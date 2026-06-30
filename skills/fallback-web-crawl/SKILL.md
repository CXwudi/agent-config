---
name: fallback-web-crawl
description: Agent Skill for web crawl via Jina. Use when there is no crawl tool, and you want to read the URL content.
---

# Jina Crawl

## Prerequisites

`JINA_API_KEY` env var is set.

`jina` CLI is available. If not, ask for user to install it. Or use the REST fallback method below.

## CLI

Start with:

```bash
jina --help
jina read --help
```

Then follow the CLI doc to fetch content from URL.

The latest CLI README is at `https://github.com/jina-ai/cli`.

## REST Fallback

When the CLI is unavailable or REST fallback is needed, use the `openapi-inspection` skill to read Jina Reader OpenAPI specs at `https://r.jina.ai/openapi.json` and `https://s.jina.ai/openapi.json`.

Then make REST API calls following the spec.
