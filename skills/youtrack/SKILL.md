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

Use the `openapi-inspection` skill to inspect the latest YouTrack API OpenAPI
specification:

`${YOUTRACK_BASE_URL}/api/openapi.json`

Then make REST API calls following the spec.
