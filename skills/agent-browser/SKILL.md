---
name: agent-browser
description: Agent Skill for browser access over a Chrome DevTools Protocol connection. Use when a task requires interacting with or inspecting live web pages, forms, or UI behavior. Prefer this skill for JS-heavy sites or when deterministic, step-by-step browser control is needed.
---

# Agent Browser

## Prerequisites

`agent-browser` command is available

A Chromium-based browser (e.g. Chrome, Edge) must be running with the
`--remote-debugging-port=<port>` flag to enable the Chrome DevTools Protocol
(CDP) connection. Port by default is `9222`, IP by default is just
`localhost`. Check if `http://<ip>:<port>/json/version` returns a websocket URL
to confirm CDP is available.

Public Internet Access is preferred but not required

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

Always connect to browser via CDP

If you are in Windows OS, follow [windows-specific-convenience](windows-specific-convenience.md) guidelines to avoid common pitfalls and ensure smooth experience.
