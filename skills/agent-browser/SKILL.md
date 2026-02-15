---
name: agent-browser
description: Agent Skill for browser access over a Chrome DevTools Protocol connection. Use when a task requires interacting with or inspecting live web pages, forms, or UI behavior. Prefer this skill for JS-heavy sites or when deterministic, step-by-step browser control is needed.
---

# Agent Browser

## Prerequisites

A Chromium-based browser (e.g. Chrome, Edge) must be running with the `--remote-debugging-port=<port>` flag to enable the Chrome DevTools Protocol (CDP) connection. Port by default is `9222`, IP by default is just `localhost`. Check if the browser is accessible at `http://<ip>:<port>/json/version` to confirm CDP is available.

Public Internet Access is preferred but not required

## References

| Reference | When to Use |
|-----------|-------------|
| [references/commands.md](references/commands.md) | Full command reference with all options |
| [references/snapshot-refs.md](references/snapshot-refs.md) | Ref lifecycle, invalidation rules, troubleshooting |
| [references/session-management.md](references/session-management.md) | Parallel sessions, state persistence, concurrent scraping |
| [references/authentication.md](references/authentication.md) | Login flows, OAuth, 2FA handling, state reuse |
| [references/video-recording.md](references/video-recording.md) | Recording workflows for debugging and documentation |
| [references/proxy-support.md](references/proxy-support.md) | Proxy configuration, geo-testing, rotating proxies |

## User Convenience

Always use connect to browser via CDP

Use `bun x agent-browser`