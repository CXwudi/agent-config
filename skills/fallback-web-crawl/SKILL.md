---
name: fallback-web-crawl
description: Agent skill of web crawl. Use only when built-in web crawl tools are unavailable or failed, and the task needs to fetch content from URL
---

# Jina Crawl

Use this skill as a fallback. Use only if there is no built-in web crawl tool,
or the built-in tool failed.

## Prerequisites

`JINA_API_KEY` env var is set.

`jina` CLI is available. If not, ask for user to install it. Or use the REST
fallback method below.

## CLI

Start with:

```bash
jina --help
jina read --help
```

Then follow the CLI doc to fetch content from URL.

The latest CLI README is at `https://github.com/jina-ai/cli`.

## REST Fallback

Jina has Reader OpenAPI specs are at `https://r.jina.ai/openapi.json` and
`https://s.jina.ai/openapi.json`. Use `curl` to fetch the spec.

Be aware that the OpenAPI spec file is large. Avoid loading the entire file into
context. Use search or `yq` to query the spec file.
