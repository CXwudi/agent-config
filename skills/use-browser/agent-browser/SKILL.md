---
name: agent-browser
description: Agent Skill for browser automation over the Chrome DevTools Protocol connection.
---

# Agent Browser

## Prerequisites

`agent-browser` command is available

Choose one of below options to connect to a browser:

### Option 1: Connect to existing browser via `--auto-connect` or `--cdp` (Preferred)

First check if a browser is already running with remote debugging enabled. Choose some of the following commands:

```
agent-browser --auto-connect get-cdp
curl -v http://localhost:9222/json/version\
agent-browser --cdp 9222 get cdp-url
agent-browser --cdp ws://127.0.0.1:9222/devtools/browser/<id> get cdp-url
agent-browser --cdp wss://your-provider.example.com/devtools/browser/<id> get cdp-url
```

### Option 2: Launch a new browser via `--remote-debugging-port <port number>`

Find in the current OS the path of any Chromium-based browser, launch it with `--remote-debugging-port <port number>` option. Prefer to use existing user profile if possible.

Then do the check mentioned in Option 1 to make sure browser is running

## Windows

If you are on Windows, read [windows-specific-convenience](windows-specific-convenience.md) before running your first `agent-browser` command.

## User Convenience

1. Start with `agent-browser --help` to see the latest manual and all available options.
1. However, do not run `agent-browser skills` as mentioned in the help message, as it provide false positive.
1. Always run `agent-browser` with `--color-scheme no-preference` to override the default light mode in agent-browser.
1. Always run `agent-browser` with at least one of `--auto-connect` or `--cdp`.
1. Do not run `agent-browser install` to install other browsers.
