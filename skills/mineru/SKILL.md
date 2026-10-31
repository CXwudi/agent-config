---
name: mineru
description: Agent Skill for parsing PDF and complex documents (preserving layout, formulas, tables, charts, etc.) into Markdown via MinerU Open API. Use when converting PDFs or documents to Markdown.
---

# MinerU

## Prerequisites

Requires MinerU API token from environment variable `MINERU_TOKEN`. If not set, ask the user to provide it.

## Usage

### Option 1: Official CLI (Preferred)

Run via `pnpm dlx mineru-open-api` (or `mineru-open-api` if installed in `$PATH`). It handles pre-signed file upload, task polling, and result extraction automatically.

Inspect available flags first:

```sh
pnpm dlx mineru-open-api extract --help
```

Examples:

```sh
# Extract local PDF or URL to Markdown on stdout
pnpm dlx mineru-open-api extract report.pdf

# Extract and save Markdown + extracted assets (images/tables/charts) to a directory
pnpm dlx mineru-open-api extract report.pdf -o ./output/
```

### Option 2: REST API

Base URL: `https://mineru.net/api/v4`
Headers: `Authorization: Bearer ${MINERU_TOKEN}`, `Content-Type: application/json`

1. Request upload URL and submit task (use `vlm` model by default for high accuracy on complex layouts, formulas, and tables):

   ```sh
   curl -sS -X POST "https://mineru.net/api/v4/file-urls/batch" \
     -H "Authorization: Bearer ${MINERU_TOKEN}" \
     -H "Content-Type: application/json" \
     -d '{"files": [{"name": "doc.pdf"}], "model_version": "vlm"}'
   ```

   For remote URLs, POST `{"url": "<url>", "model_version": "vlm"}` to `/extract/task` (single) or `{"files": [{"url": "<url>"}], "model_version": "vlm"}` to `/extract/task/batch` instead.

2. Upload the local file via `PUT` to the returned `data.file_urls[0]` (do not set `Authorization` or `Content-Type` headers on the `PUT` request; parsing starts automatically once uploaded):

   ```sh
   curl -sS -X PUT -T "doc.pdf" "<file_url>"
   ```

3. Poll `GET /extract-results/batch/{batch_id}` (or `GET /extract/task/{task_id}`) until `state` is `done`, then download and unzip `full_zip_url` to get `full.md` and extracted assets.

## Notes

- Official API documentation: `https://mineru.net/apiManage/docs`
- Precision Extract API limits: max 200 MB / 200 pages per file.
- Remote URL mode cannot access GitHub or AWS URLs directly due to server network restrictions; download them locally and use local file upload instead.
