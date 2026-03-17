---
name: gemini-files
description: Agent Skill for uploading files to Gemini File API and questioning them with Gemini models. Use when a task requires analyzing, transcribing, or asking questions about files (video, audio, images, PDFs, documents, etc.)
---
# Gemini Files

## Prerequisites

Set `GEMINI_API_KEY` in the environment or pass `--api-key <key>` on the
command line.

Global options:

- `--api-key KEY`: Gemini API key. Falls back to `GEMINI_API_KEY`.
- `--json`: Return structured JSON instead of plain text.

## Commands

- `upload`: Upload a local file and wait until it becomes `ACTIVE` or
  `FAILED`. Example: `uv run scripts/gemini_files.py upload ./clip.mp4`
- `query`: Ask Gemini a question about an uploaded file. Example:
  `uv run scripts/gemini_files.py query files/abc123 "Summarize this
  document"`
- `list`: List uploaded Gemini files. Example:
  `uv run scripts/gemini_files.py list`
- `status`: Show the state and metadata for an uploaded file. Example:
  `uv run scripts/gemini_files.py status files/abc123`

### Upload

Usage:

```bash
uv run scripts/gemini_files.py upload <file-path> [--timeout SECONDS]
```

Examples:

```bash
uv run scripts/gemini_files.py upload ./meeting.mp4
uv run scripts/gemini_files.py upload ./report.pdf --timeout 600
uv run scripts/gemini_files.py --json upload ./song.wav
```

### Query

Usage:

```bash
uv run scripts/gemini_files.py query <file-name> "<question>" \
  [--model MODEL] [--system-prompt "..."]
```

Examples:

```bash
uv run scripts/gemini_files.py query files/abc123 "Transcribe this video."
uv run scripts/gemini_files.py query files/abc123 \
  "List the action items in this PDF."
uv run scripts/gemini_files.py query files/abc123 \
  "Identify the chorus timestamps." \
  --system-prompt "Answer as a music analyst."
uv run scripts/gemini_files.py --json query files/abc123 \
  "Describe this image." \
  --model gemini-3.1-pro-preview
```

### List

Usage:

```bash
uv run scripts/gemini_files.py list
```

Examples:

```bash
uv run scripts/gemini_files.py list
uv run scripts/gemini_files.py --json list
```

### Status

Usage:

```bash
uv run scripts/gemini_files.py status <file-name>
```

Examples:

```bash
uv run scripts/gemini_files.py status files/abc123
uv run scripts/gemini_files.py --json status files/abc123
```

## Common Workflows

### Video transcription

```bash
uv run scripts/gemini_files.py upload ./meeting.mp4
uv run scripts/gemini_files.py query files/abc123 \
  "Transcribe this video with speaker changes and timestamps when possible."
```

### Document analysis

```bash
uv run scripts/gemini_files.py upload ./contract.pdf
uv run scripts/gemini_files.py query files/abc123 \
  "Summarize the key obligations and deadlines in this document."
```

### Image understanding

```bash
uv run scripts/gemini_files.py upload ./diagram.png
uv run scripts/gemini_files.py query files/abc123 \
  "Explain the architecture shown in this image."
```

### Multi-question analysis

```bash
uv run scripts/gemini_files.py upload ./research-paper.pdf
uv run scripts/gemini_files.py query files/abc123 "Summarize the paper."
uv run scripts/gemini_files.py query files/abc123 "What are the main limitations?"
uv run scripts/gemini_files.py query files/abc123 "Extract the evaluation metrics."
```

### Audio analysis

```bash
uv run scripts/gemini_files.py upload ./song.wav
uv run scripts/gemini_files.py query files/abc123 \
  "Identify the chorus section timestamps and describe the overall mood."
```

## Notes

- Gemini uploaded files expire after roughly 48 hours.
- Large files can stay in `PROCESSING` for a while. Use `status` to check
  progress.
- The default model is `gemini-3.1-pro-preview`. Override it with `--model`
  when needed.
- If Google rotates preview model names, prefer setting `--model` explicitly
  instead of editing the script in the middle of a task.
