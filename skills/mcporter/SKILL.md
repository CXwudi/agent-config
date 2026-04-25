---
name: mcporter
description: Agent Skill for calling MCP servers through MCPorter. Use when need to call MCP tools.
---

# MCPorter

Use MCPorter as a config-free bridge from shell commands to MCP tools.

## Caller Contract

The caller must provide:

- A stable `--name <slug>` for the MCP target.
- Exactly one explicit transport target:
  - `--http-url <url>` for HTTP MCP servers.
  - `--stdio "<command>"` for STDIO MCP servers.
- The goal, expected tool, or enough task context to choose a tool from the live
  schema.

Do not rely on local configured MCP server names. Do not generate or use
checked-in MCPorter CLIs.

## Workflow

1. Inspect the target before calling any tool.
2. Treat the live listing/schema as the source of truth for tool names,
   parameter names, required fields, enum values, nested object shapes, and
   return shape hints.
3. Build the tool call from the inspected signature. Prefer function-call syntax
   because it mirrors MCPorter's listed signatures.
4. Repeat the same `--name` and explicit transport target for `list`, `call`,
   and `auth` commands.
5. If the target requires session or auth setup, run `mcporter auth` with the
   same `--name` and transport target, then retry the original list or call.

## Inspect Commands

HTTP target:

```bash
pnpm dlx mcporter list \
  --http-url https://mcp.example.com/mcp \
  --name example \
  --schema
```

STDIO target:

```bash
pnpm dlx mcporter list \
  --stdio "bun run ./server.ts" \
  --name example \
  --schema
```

If optional fields are hidden or the task needs a less common parameter, inspect
again with `--all-parameters`.

## Call Commands

Prefer named function-call syntax. Quote the whole expression with single quotes
so the shell preserves parentheses, commas, and nested structures.

HTTP target:

```bash
pnpm dlx mcporter call \
  --http-url https://mcp.example.com/mcp \
  --name example \
  'tool_name(requiredParam: "value")'
```

STDIO target:

```bash
pnpm dlx mcporter call \
  --stdio "bun run ./server.ts" \
  --name example \
  'tool_name(requiredParam: "value")'
```

For simple flat arguments, key/value syntax is acceptable when it is clearer:

```bash
pnpm dlx mcporter call \
  --http-url https://mcp.example.com/mcp \
  --name example \
  tool_name requiredParam=value
```

Use `--args '{...}'` when the caller already has a JSON payload or shell quoting
would make a nested call expression fragile.

## Auth Or Session Setup

Use the same explicit target and name for setup:

```bash
pnpm dlx mcporter auth \
  --http-url https://mcp.example.com/mcp \
  --name example
```

For STDIO, replace `--http-url` with the same `--stdio` command used for listing
and calls.

## Safety And Context Rules

- Do not invent tools, arguments, enum values, or output fields. Verify them
  from `mcporter list` output or label them as caller-provided assumptions.
- Do not use bare configured selectors such as `server.tool`; require explicit
  `--http-url` or `--stdio` plus `--name`.
- Do not pass `--persist` or write MCPorter configuration unless the caller
  explicitly requests persistence.
- Do not use `generate-cli` for this skill. Live inspection keeps MCP server
  updates simple and avoids checked-in generated artifacts.
- If multiple tools could satisfy the goal, choose the best candidate from the
  schema and briefly explain the tradeoff.
- If listing or calling fails, report the command attempted, the failure, and
  the next concrete thing that can be done.
