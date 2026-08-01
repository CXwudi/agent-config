---
name: bocha
description: Agent Skill for web search via Bocha.
---

# Bocha

## Prerequisites

`BOCHA_API_KEY` env var is available.

## Usage

Use the `mcporter` skill with this explicit MCP target:

- Name: `bocha`
- HTTP URL: `https://mcp.bochaai.com/mcp`
- Header: `Authorization: Bearer <BOCHA_API_KEY>`

Then make MCP calls through `mcporter`.

