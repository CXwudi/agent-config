---
name: fallback-web-search
description: Agent skill of web search. Use only when built-in web search tools are unavailable or failed, and the task requires web search
---

# Exa Search

Use this skill as a fallback. Only if there is no built-in web search tool, or
the build-in search tool can not provide helpful results.

## Prerequisites

`EXA_API_KEY` env var is set.

## Usage

Use `curl` to fetch the latest official Search API OpenAPI specification:

`https://raw.githubusercontent.com/exa-labs/openapi-spec/refs/heads/master/exa-openapi-spec.yaml`

Be aware that the OpenAPI spec can be large. Avoid loading the entire file into
context. Use search or `yq` to query the spec file.
