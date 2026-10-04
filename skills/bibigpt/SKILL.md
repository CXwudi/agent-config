---
name: bibigpt
description: Agent Skill for BibiGPT via RestAPI. Use when need information (content summary, question answering, etc) about Bilibili/Youtube/Tiktok online videos, or local video/audio files
compatibility: Requires network access to the BibiGPT and curl.
---

# BibiGPT

## Prerequisites

Require API key from environment variables `BIBIGPT_API_KEY`. If not set, ask the user to provide it.

## Usage

Use the `openapi-inspection` skill to inspect the latest BibiGPT API OpenAPI specification:

`https://api.bibigpt.co/api/openapi.json`

Then make REST API calls following the spec.

### Not execlusive summary of the API endpoints

The API can:

- Summarize YouTube / Bilibili / TikTok links
- /file Summarize local video files
- /subtitle Extract subtitles
- /chat Chat with audio/video content
- More APIs: audio / rap / song / video

Do check the OpenAPI spec for more details and how to use.
