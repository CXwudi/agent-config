---
name: mineru
description: Agent Skill for parsing PDF and documents into Markdown via MinerU Open API. Use when converting PDFs or documents to Markdown. Also use when the PDF or document is scanned copy, or contains complex layouts. Also use when you can not get meaningful content from it when using other tools.
---

# MinerU

## Prerequisites

environment variable `MINERU_TOKEN` is available. If not set, ask the user to provide it.

## Usage

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

3. Poll `GET /extract-results/batch/{batch_id}` (or `GET /extract/task/{task_id}`) until `state` is `done`, then download and unzip `full_zip_url` to get `full.md` and extracted assets. (both fields are somewhere in the response JSON)

## Notes

- Official API documentation: `https://mineru.net/apiManage/docs`
- Precision Extract API limits: max 200 MB / 200 pages per file.
  - You can split large files into smaller files
- Remote URL mode cannot access GitHub or AWS URLs directly due to server network restrictions
  - You can download locally and use local file upload instead.
