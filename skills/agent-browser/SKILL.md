---
name: agent-browser
description: Agent Skill for browser automation over the Chrome DevTools Protocol connection. Use when a task requires interacting with or inspecting live web pages, forms, UI behavior, or any scraping tasks like data extraction, form filling, etc, or any browser automation tasks.
---

# Agent Browser

## Prerequisites

`agent-browser` command is available

Public Internet Access is preferred but not required

### Browser Connection

A Chromium-based browser (e.g. Chrome, Edge, Chromium, Brave) must be running

Prefer `--auto-connect` first. If auto-discovery fails or you already know the
exact CDP endpoint, use `--cdp`.

### Option 1: `--auto-connect` (Preferred)

Use `--auto-connect` when a supported Chromium-based browser is already running
with remote debugging enabled and you want `agent-browser` to discover the CDP
endpoint automatically.

It is most reliable for Chrome, Chrome Canary, and Chromium in default user
data locations where `DevToolsActivePort` can be discovered. Other
Chromium-based browsers may still work if they expose CDP on common local
ports such as `9222` or `9229`.

Example: `agent-browser --auto-connect tab`

### Option 2: `--cdp` (Explicit)

Use `--cdp` when you already know the CDP endpoint and want a predictable
connection.

This is the best choice for a known local port, a full CDP WebSocket URL, or a
browser-as-a-service provider over `ws://` or `wss://`.

Use `curl` to check if `http://<ip>:<port>/json/version` returns a websocket
URL when connecting by local port.

Examples:

```bash
agent-browser --cdp 9222 tab
agent-browser --cdp ws://127.0.0.1:9222/devtools/browser/<id> tab
agent-browser --cdp wss://your-provider.example.com/devtools/browser/<id> tab
```

If both `--auto-connect` and `--cdp` fail, notify the user to start their
browser with remote debugging enabled.

## Windows

If you are on Windows, read
[windows-specific-convenience](windows-specific-convenience.md) before
running your first `agent-browser` command.

## References

| Reference | When to Use | Local Fallback |
| --------- | ----------- | -------------- |
| [commands.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/commands.md) | Full command reference with all options | [references/commands.md](references/commands.md) |
| [snapshot-refs.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/snapshot-refs.md) | Ref lifecycle, invalidation rules, troubleshooting | [references/snapshot-refs.md](references/snapshot-refs.md) |
| [session-management.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/session-management.md) | Parallel sessions, state persistence, concurrent scraping | [references/session-management.md](references/session-management.md) |
| [authentication.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/authentication.md) | Login flows, OAuth, 2FA handling, state reuse | [references/authentication.md](references/authentication.md) |
| [video-recording.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/video-recording.md) | Recording workflows for debugging and documentation | [references/video-recording.md](references/video-recording.md) |
| [profiling.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/profiling.md) | Chrome DevTools profiling for performance analysis | [references/profiling.md](references/profiling.md) |
| [proxy-support.md](https://raw.githubusercontent.com/vercel-labs/agent-browser/main/skills/agent-browser/references/proxy-support.md) | Proxy configuration, geo-testing, rotating proxies | [references/proxy-support.md](references/proxy-support.md) |

A local copy of each reference is available as a fallback, but it may be outdated.

## User Convenience

1. Prefer `--cdp`, and use `--auto-connect` as the fallback path.
2. Use `--color-scheme no-preference` to override the default light mode in agent-browser
