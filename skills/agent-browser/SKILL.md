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

Only `--auto-connect` and `--cdp` connection are allowed.
If both options fail, notify the user to fix it.

### Option 1: `--auto-connect` (Preferred)

This will attempt to automatically find the debugging port and connect to it.

Example: `agent-browser --auto-connect tab`

### Option 2: `--cdp` (Explicit)

Use `--cdp` when you already know a CDP endpoint.

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

## User Convenience

1. Start with `agent-browser --help` to see the latest manual and all available options.
1. However, do not run `agent-browser skills` as mentioned in the help message, as it provide false positive.
1. Always run `agent-browser` with `--color-scheme no-preference` to override the default light mode in agent-browser.
1. Always run `agent-browser` with at least one of `--auto-connect` or `--cdp`.
1. Do not run `agent-browser install` to install other browsers.
