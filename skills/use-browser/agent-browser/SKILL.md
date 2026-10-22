---
name: agent-browser
description: Agent Skill for browser automation over the Chrome DevTools Protocol connection.
---

# Agent Browser

## Prerequisites

`agent-browser` command is available

Choose one of below options to connect to a browser:

### Connect to existing browser via `--auto-connect` or `--cdp` (Preferred)

First check if a browser is already running with remote debugging enabled. Choose some of the following commands:

```
agent-browser --auto-connect get-cdp
curl -v http://localhost:9222/json/version\
agent-browser --cdp 9222 get cdp-url
agent-browser --cdp ws://127.0.0.1:9222/devtools/browser/<id> get cdp-url
agent-browser --cdp wss://your-provider.example.com/devtools/browser/<id> get cdp-url
```

### If no browser with remote debugging enabled is found

Find in the current OS the path of any Chromium-based browser,
launch it with `<browser executable> --remote-debugging-port <port number>`.
Then connect to it with `--auto-connect` or `--cdp`.

Note: 
- Do not use `agent-browser` to launch the browser.
- Do not specify any profile to launch, use user's existing profile.

## Windows

If you are on Windows, read [windows-specific-convenience](windows-specific-convenience.md) before running your first `agent-browser` command.

## Notes

1. Start with `agent-browser --help` to see the latest manual and all available options.
1. However, do not run `agent-browser skills` as mentioned in the help message, as it provide false positive.
1. Always run `agent-browser` with `--color-scheme no-preference` to override the default light mode in agent-browser.
1. Always run `agent-browser` with at least one of `--auto-connect` or `--cdp`.
1. Do not run `agent-browser install` to install other browsers.
