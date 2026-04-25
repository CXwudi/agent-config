---
name: fallback-web-search
description: Agent Skill for web search. Use only when built-in web search tools are unavailable or failed, and the task requires web search
---

# Exa Search

Use this skill as a fallback. Only if there is no built-in web search tool, or
the build-in search tool can not provide helpful results.

## Prerequisites

`EXA_API_KEY` env var is set.

## Usage

Use the `openapi-inspection` skill to inspect the latest official Search API
OpenAPI specification:

`https://raw.githubusercontent.com/exa-labs/openapi-spec/refs/heads/master/exa-openapi-spec.yaml`

Then make REST API calls following the spec.
