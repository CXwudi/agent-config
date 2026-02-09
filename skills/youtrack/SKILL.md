---
name: youtrack
description: Agent Skill for YouTrack via RestAPI. Use when interacting with YouTrack.
compatibility: Requires network access to the YouTrack instance and curl.
---

# YouTrack

Retrieve the YouTrack base URL and API key from environment variables `YOUTRACK_BASE_URL` and `YOUTRACK_API_KEY`.
If not set, you can ask the user to provide them.

Then, use `curl` or web crawl tool to fetch the latest YouTrack API OpenAPI specification at `${YOUTRACK_BASE_URL}/api/openapi.json`, with `Authorization: Bearer ${YOUTRACK_API_KEY}`. If offline, a copy of the specification is available at `references/youtrack_openapi.json`, but it may be outdated. So prefer fetching from network if possible.

Once you get the OpenAPI spec, 