---
name: deepwiki
description: Agent Skill for DeepWiki via MCPorter. Use when answering questions about a GitHub repository's architecture, codebase structure, or implementation details.
---

# DeepWiki

## Usage

Use the `mcporter` skill with this explicit MCP target:

- Name: `deepwiki`
- HTTP URL: `https://mcp.deepwiki.com/mcp`

Then make MCP calls through `mcporter`.

Prefer `ask_question` for focused questions. Use `read_wiki_structure` to
discover topics and `read_wiki_contents` to read the generated docs.
