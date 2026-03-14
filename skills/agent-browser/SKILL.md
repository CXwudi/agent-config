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


Prefer `--cdp` first. If `--cdp` is unavailable or inconvenient, try
`--auto-connect`.

### Option 1: `--cdp` (Preferred)

A Chromium-based browser (e.g. Chrome, Edge, Chromium, Brave) can be connected
directly over the Chrome DevTools Protocol (CDP) when it is running with the
`--remote-debugging-port=<port>` flag. Port by default is `9222`, IP by
default is just `localhost`.

Use `curl` to check if `http://<ip>:<port>/json/version` returns a websocket URL
to confirm CDP is available.

### Option 2: `--auto-connect` (Fallback)

For some Chromium-based browsers, especially Chrome or Chromium `144+`,
`agent-browser --auto-connect` can discover a running browser without
explicitly providing a port.

This requires remote debugging to already be enabled for that browser session.
In practice, `agent-browser` usually relies on the browser exposing a
discoverable DevTools endpoint, such as a `DevToolsActivePort` file in the
browser's user data directory. The exact setup flow and file location vary by
browser and operating system.

If both `--cdp` and `--auto-connect` failed, notify the user to start
their browser with remote debugging enabled.

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
