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
agent-browser --auto-connect get cdp-url
curl --fail --silent --show-error http://127.0.0.1:9222/json/version
agent-browser --cdp 9222 get cdp-url
agent-browser --cdp ws://127.0.0.1:9222/devtools/browser/<id> get cdp-url
agent-browser --cdp wss://your-provider.example.com/devtools/browser/<id> get cdp-url
```

### If no browser with remote debugging enabled is found

Find in the current OS the path of any Chromium-based browser.
Make sure no other browser is running, if there is, ask the user if it is safe to close it. When user confirms, close it gently.
Then launch it with `<browser executable> --remote-debugging-port <port number>`.

Then you can use `agent-browser` to connect to it with `--auto-connect` or `--cdp`.

Note: 
- Do not use `agent-browser` to launch the browser.
- You must use the user's existing profile, in order to reuse the existing session and cookies. Do not use a new profile. Do not use a clone of the existing profile.

## Windows

If you are on Windows, read [windows-specific-convenience](windows-specific-convenience.md) before running your first `agent-browser` command.

## Notes

1. Start with `agent-browser --help` to see the latest manual and all available options.
1. However, do not run `agent-browser skills` as mentioned in the help message, as it provide false positive.
1. Always run `agent-browser` with `--color-scheme no-preference` to override the default light mode in agent-browser.
1. Always run `agent-browser` with at least one of `--auto-connect` or `--cdp`.
1. Do not run `agent-browser install` to install other browsers.
