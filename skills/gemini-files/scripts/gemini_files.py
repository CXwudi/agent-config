# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "google-genai>=1.52",
# ]
# ///
"""Upload files to Gemini and query them from the command line."""

from __future__ import annotations

import argparse
import json
import logging
import os
import sys
import time
from collections.abc import Sequence
from pathlib import Path
from typing import Final

from google import genai
from google.genai import errors, types

DEFAULT_MODEL: Final[str] = "gemini-3.1-pro-preview"
DEFAULT_TIMEOUT_SECONDS: Final[int] = 300
POLL_INTERVAL_SECONDS: Final[int] = 2

logger = logging.getLogger(__name__)


class GeminiFilesError(RuntimeError):
  """Raised for user-facing CLI errors."""


def create_client(api_key: str | None) -> genai.Client:
  """Create a Gemini client from CLI or environment credentials."""
  resolved_api_key = api_key or os.environ.get("GEMINI_API_KEY")
  if not resolved_api_key:
    raise GeminiFilesError(
      "Missing Gemini API key. Pass --api-key or set GEMINI_API_KEY."
    )
  return genai.Client(api_key=resolved_api_key)


def file_to_dict(file_obj: types.File) -> dict[str, object]:
  """Serialize a Gemini file to JSON-friendly data."""
  return file_obj.model_dump(mode="json", exclude_none=True)


def usage_to_dict(
  usage: types.GenerateContentResponseUsageMetadata | None,
) -> dict[str, object] | None:
  """Serialize usage metadata when the model returned it."""
  if usage is None:
    return None
  return usage.model_dump(mode="json", exclude_none=True)


def get_file_state(file_obj: types.File) -> str:
  """Return a stable string for the Gemini file state."""
  state = file_obj.state
  if state is None:
    return "STATE_UNSPECIFIED"
  if hasattr(state, "value"):
    return str(state.value)
  if hasattr(state, "name"):
    return str(state.name)
  return str(state)


def get_resource_name(file_obj: types.File) -> str:
  """Return the Gemini resource name or raise a clear error."""
  if not file_obj.name:
    raise GeminiFilesError("Gemini returned a file without a resource name.")
  return file_obj.name


def get_file_error_message(file_obj: types.File) -> str | None:
  """Extract a readable error message from a failed Gemini file."""
  if file_obj.error is None:
    return None

  if hasattr(file_obj.error, "model_dump"):
    error_data = file_obj.error.model_dump(mode="json", exclude_none=True)
    if isinstance(error_data, dict) and "message" in error_data:
      return str(error_data["message"])
    return json.dumps(error_data, ensure_ascii=False, sort_keys=True)

  return str(file_obj.error)


def wait_for_file_activation(
  client: genai.Client,
  file_obj: types.File,
  timeout_seconds: int,
) -> types.File:
  """Poll Gemini until the file becomes ACTIVE or fails."""
  if timeout_seconds <= 0:
    raise GeminiFilesError("--timeout must be greater than 0.")

  resource_name = get_resource_name(file_obj)
  deadline = time.monotonic() + timeout_seconds
  current_file = file_obj

  while get_file_state(current_file) == "PROCESSING":
    if time.monotonic() >= deadline:
      raise GeminiFilesError(
        f"Timed out after {timeout_seconds}s waiting for {resource_name} to "
        "become ACTIVE. Retry with a larger --timeout for large files."
      )

    logger.debug(
      "Waiting for %s to become ACTIVE; current state=%s",
      resource_name,
      get_file_state(current_file),
    )
    time.sleep(POLL_INTERVAL_SECONDS)
    current_file = client.files.get(name=resource_name)

  file_state = get_file_state(current_file)
  if file_state == "FAILED":
    error_message = get_file_error_message(current_file)
    suffix = f": {error_message}" if error_message else ""
    raise GeminiFilesError(
      f"File processing failed for {resource_name}{suffix}"
    )

  if file_state != "ACTIVE":
    raise GeminiFilesError(
      f"Unexpected file state for {resource_name}: {file_state}"
    )

  return current_file


def format_json(data: object) -> str:
  """Render structured output as pretty JSON."""
  return json.dumps(data, ensure_ascii=False, indent=2, sort_keys=True)


def format_file_table(files: Sequence[types.File]) -> str:
  """Render uploaded file metadata as a simple plain-text table."""
  rows = [
    {
      "name": file_obj.name or "-",
      "state": get_file_state(file_obj),
      "mime_type": file_obj.mime_type or "-",
      "uri": file_obj.uri or "-",
    }
    for file_obj in files
  ]

  if not rows:
    return "No files found."

  headers = ("name", "state", "mime_type", "uri")
  widths = {
    header: max(len(header), *(len(row[header]) for row in rows))
    for header in headers
  }

  def format_row(row: dict[str, str]) -> str:
    return "  ".join(row[header].ljust(widths[header]) for header in headers)

  header_row = format_row({header: header for header in headers})
  separator_row = "  ".join("-" * widths[header] for header in headers)

  body_rows = [format_row(row) for row in rows]
  return "\n".join([header_row, separator_row, *body_rows])


def format_status_value(value: object) -> str:
  """Render a metadata value for human-readable output."""
  if isinstance(value, (dict, list)):
    return json.dumps(value, ensure_ascii=False, sort_keys=True)
  return str(value)


def format_file_status(file_obj: types.File) -> str:
  """Render detailed file metadata as readable plain text."""
  file_data = file_to_dict(file_obj)
  field_labels = {
    "name": "Name",
    "display_name": "Display name",
    "state": "State",
    "mime_type": "MIME type",
    "size_bytes": "Size bytes",
    "create_time": "Created",
    "update_time": "Updated",
    "expiration_time": "Expires",
    "uri": "URI",
    "download_uri": "Download URI",
    "sha256_hash": "SHA256",
    "source": "Source",
    "video_metadata": "Video metadata",
    "error": "Error",
  }
  ordered_fields = (
    "name",
    "display_name",
    "state",
    "mime_type",
    "size_bytes",
    "create_time",
    "update_time",
    "expiration_time",
    "uri",
    "download_uri",
    "sha256_hash",
    "source",
    "video_metadata",
    "error",
  )

  lines = [
    f"{field_labels[field]}: {format_status_value(file_data[field])}"
    for field in ordered_fields
    if field in file_data
  ]
  return "\n".join(lines) if lines else "No metadata available."


def extract_response_text(response: types.GenerateContentResponse) -> str:
  """Extract the text portion of a Gemini model response."""
  try:
    text = response.text
  except ValueError:
    text = None

  if text:
    stripped_text = text.strip()
    if stripped_text:
      return stripped_text

  if response.candidates:
    parts: list[str] = []
    for candidate in response.candidates:
      if candidate.content is None or candidate.content.parts is None:
        continue
      for part in candidate.content.parts:
        if part.text:
          parts.append(part.text)

    combined_text = "\n".join(parts).strip()
    if combined_text:
      return combined_text

  raise GeminiFilesError("Model returned no text response.")


def emit_result(text_output: str, json_data: object, json_mode: bool) -> None:
  """Print either plain text or JSON output."""
  if json_mode:
    print(format_json(json_data))
    return
  print(text_output)


def cmd_upload(
  client: genai.Client,
  args: argparse.Namespace,
) -> tuple[str, dict[str, object]]:
  """Upload a file and wait for Gemini to finish processing it."""
  file_path = Path(args.file_path).expanduser()
  if not file_path.exists():
    raise GeminiFilesError(f"File not found: {file_path}")
  if not file_path.is_file():
    raise GeminiFilesError(f"Not a regular file: {file_path}")

  uploaded_file = client.files.upload(file=file_path)
  active_file = wait_for_file_activation(client, uploaded_file, args.timeout)

  resource_name = get_resource_name(active_file)
  if not active_file.uri:
    raise GeminiFilesError(
      f"Gemini did not return a file URI for {resource_name}."
    )

  return (
    f"Uploaded: {resource_name} (uri: {active_file.uri})",
    file_to_dict(active_file),
  )


def cmd_query(
  client: genai.Client,
  args: argparse.Namespace,
) -> tuple[str, dict[str, object]]:
  """Ask Gemini a question about an uploaded file."""
  file_obj = client.files.get(name=args.file_name)
  resource_name = get_resource_name(file_obj)
  file_state = get_file_state(file_obj)

  if file_state == "PROCESSING":
    raise GeminiFilesError(
      f"{resource_name} is still processing. Retry later or use the status "
      "command."
    )
  if file_state == "FAILED":
    error_message = get_file_error_message(file_obj)
    suffix = f": {error_message}" if error_message else ""
    raise GeminiFilesError(f"{resource_name} is in FAILED state{suffix}")
  if file_state != "ACTIVE":
    raise GeminiFilesError(
      f"{resource_name} is not ACTIVE. Current state: {file_state}"
    )
  if not file_obj.uri:
    raise GeminiFilesError(
      f"Gemini did not return a file URI for {resource_name}."
    )

  config = None
  if args.system_prompt:
    config = types.GenerateContentConfig(
      system_instruction=args.system_prompt
    )

  response = client.models.generate_content(
    model=args.model,
    contents=[
      types.Part.from_text(text=args.question),
      types.Part.from_uri(
        file_uri=file_obj.uri,
        mime_type=file_obj.mime_type,
      ),
    ],
    config=config,
  )
  response_text = extract_response_text(response)

  json_data: dict[str, object] = {
    "model": args.model,
    "response": response_text,
  }
  if response.model_version:
    json_data["model_version"] = response.model_version

  usage = usage_to_dict(response.usage_metadata)
  if usage is not None:
    json_data["usage"] = usage

  return response_text, json_data


def cmd_list(
  client: genai.Client,
  args: argparse.Namespace,
) -> tuple[str, list[dict[str, object]]]:
  """List uploaded Gemini files."""
  del args
  files = list(client.files.list())
  return format_file_table(files), [file_to_dict(file_obj) for file_obj in files]


def cmd_status(
  client: genai.Client,
  args: argparse.Namespace,
) -> tuple[str, dict[str, object]]:
  """Show metadata for a single uploaded Gemini file."""
  file_obj = client.files.get(name=args.file_name)
  return format_file_status(file_obj), file_to_dict(file_obj)


def add_global_options(
  parser: argparse.ArgumentParser,
  *,
  suppress_defaults: bool = False,
) -> None:
  """Register CLI options shared by every command."""
  api_key_kwargs: dict[str, object] = {
    "help": "Gemini API key. Falls back to GEMINI_API_KEY.",
  }
  json_kwargs: dict[str, object] = {
    "action": "store_true",
    "dest": "json_mode",
    "help": "Output structured JSON instead of plain text.",
  }

  if suppress_defaults:
    api_key_kwargs["default"] = argparse.SUPPRESS
    json_kwargs["default"] = argparse.SUPPRESS

  parser.add_argument("--api-key", **api_key_kwargs)
  parser.add_argument("--json", **json_kwargs)


def build_parser() -> argparse.ArgumentParser:
  """Build the CLI argument parser."""
  parser = argparse.ArgumentParser(
    description="Upload files to Gemini File API and query them.",
  )
  add_global_options(parser)

  shared_subparser = argparse.ArgumentParser(add_help=False)
  add_global_options(shared_subparser, suppress_defaults=True)

  subparsers = parser.add_subparsers(
    dest="command",
    metavar="command",
    required=True,
  )

  upload_parser = subparsers.add_parser(
    "upload",
    help="Upload a local file to Gemini.",
    parents=[shared_subparser],
  )
  upload_parser.add_argument("file_path", help="Path to a local file.")
  upload_parser.add_argument(
    "--timeout",
    type=int,
    default=DEFAULT_TIMEOUT_SECONDS,
    help=(
      "Maximum seconds to wait for Gemini to finish processing "
      f"(default: {DEFAULT_TIMEOUT_SECONDS})."
    ),
  )
  upload_parser.set_defaults(handler=cmd_upload)

  query_parser = subparsers.add_parser(
    "query",
    help="Ask a question about an uploaded Gemini file.",
    parents=[shared_subparser],
  )
  query_parser.add_argument(
    "file_name",
    help="Gemini file resource name, usually something like files/abc123.",
  )
  query_parser.add_argument("question", help="Question to ask about the file.")
  query_parser.add_argument(
    "--model",
    default=DEFAULT_MODEL,
    help=f"Gemini model to use (default: {DEFAULT_MODEL}).",
  )
  query_parser.add_argument(
    "--system-prompt",
    help="Optional system instruction for the Gemini model.",
  )
  query_parser.set_defaults(handler=cmd_query)

  list_parser = subparsers.add_parser(
    "list",
    help="List uploaded Gemini files.",
    parents=[shared_subparser],
  )
  list_parser.set_defaults(handler=cmd_list)

  status_parser = subparsers.add_parser(
    "status",
    help="Show metadata for an uploaded Gemini file.",
    parents=[shared_subparser],
  )
  status_parser.add_argument(
    "file_name",
    help="Gemini file resource name, usually something like files/abc123.",
  )
  status_parser.set_defaults(handler=cmd_status)

  return parser


def main(argv: Sequence[str] | None = None) -> int:
  """Run the CLI."""
  parser = build_parser()
  args = parser.parse_args(list(argv) if argv is not None else None)

  try:
    client = create_client(args.api_key)
    text_output, json_data = args.handler(client, args)
    emit_result(text_output, json_data, args.json_mode)
    return 0
  except GeminiFilesError as exc:
    print(f"Error: {exc}", file=sys.stderr)
    return 1
  except KeyboardInterrupt:
    print("Interrupted.", file=sys.stderr)
    return 130
  except (errors.ClientError, errors.ServerError, errors.APIError) as exc:
    print(f"Gemini API error: {exc}", file=sys.stderr)
    return 1


if __name__ == "__main__":
  raise SystemExit(main())
