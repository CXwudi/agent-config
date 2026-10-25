---
name: cua
description: Agent Skill for Computer Use via CUA
---

# CUA

## Prerequisites

`cua-driver` is available on PATH.

Run following to verify version, autostart status, daemon status, and Windows UIA health of `cua-driver`:

```sh
cua-driver --version
cua-driver autostart status
cua-driver status
cua-driver doctor
```

If daemon is not running, run:

```sh
cua-driver autostart kick
```

## Usage

Start with:

```sh
cua-driver --help
cua-driver list-tools
```

to understand the usage.
You may likely need to run more commands to understand the usage of `cua-driver` and its tools.

## Commands to Avoid

Do not run these commands so that `~/.agents/skills` stay untouched, and no MCP config is needed:

- `cua-driver skills install`
- `cua-driver mcp-config ...`
- `cua-driver mcp`

## Notes

- Here is some diagnostic useful for you, read it when you get stuck or anything wired on using `cua-driver`: [`cua-driver-findings.md`](references/cua-driver-findings.md)
