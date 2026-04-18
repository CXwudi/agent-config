---
name: youtrack
description: Agent Skill for YouTrack via RestAPI. Use when interacting with YouTrack.
compatibility: Requires network access to the YouTrack instance and curl.
---

# YouTrack

## Prerequisites

Retrieve the YouTrack base URL and API key from environment variables
`YOUTRACK_BASE_URL` and `YOUTRACK_API_KEY`. If not set, you can ask the user to
provide them.

## Usage

Use `curl` to fetch the latest YouTrack API OpenAPI specification from
`${YOUTRACK_BASE_URL}/api/openapi.json`, with
`Authorization: Bearer ${YOUTRACK_API_KEY}`.

Be aware that the OpenAPI spec file is large. Avoid loading the entire file into
context. Use search or `yq` to query the spec file.
