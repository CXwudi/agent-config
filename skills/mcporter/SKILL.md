---
name: mcporter
description: Agent Skill for calling MCP servers through MCPorter. Use when need to call MCP tools.
---

# MCPorter

Use MCPorter as a config-free bridge from shell commands to MCP tools.

Start with:

```
pnpm dlx mcporter --help
pnpm dlx mcporter list --help
pnpm dlx mcporter call --help
```

To understand how to use `mcporter` to call MCP servers.

Prefer to use `pnpm dlx mcporter call` to call MCP server tool directly.

## Note

- Do not invent tools, arguments, enum values, or output fields. Verify them from `mcporter list` output or label them as caller-provided assumptions.
- When calling `mcporter`, provide:
  - A stable `--name <slug>` for the MCP target, and reuse the same name for the same MCP server.
  - Exactly one explicit transport target:
    - `--http-url <url>` for HTTP MCP servers.
    - `--stdio "<command>"` for STDIO MCP servers.
