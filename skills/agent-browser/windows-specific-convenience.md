# Windows Specific Convenience

You must follow these to smoothly run `agent-browser` on Windows.

## 1. Use writable socket directory only if needed

In a normal local shell, `~/.agent-browser` is usually writable. In sandboxed
environments such as Codex, it may not be. If you hit socket dir visibility,
cleanup, or write-permission issues, set a known writable directory:

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="$env:TEMP\agent-browser-sock"
```

## 2. Keep `AGENT_BROWSER_SOCKET_DIR` consistent per workflow

`AGENT_BROWSER_SOCKET_DIR` affects where session metadata (`*.pid`, `*.port`) is
stored. If you switch this value between commands, `session list` may not show
sessions started under the other directory.

Pick one strategy for the whole workflow:

- leave it unset to use `~/.agent-browser`
- set a custom directory once and reuse it for every command

Bootstrap environment once before first command (Windows):

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="$env:TEMP\agent-browser-sock" # Set this if needed
agent-browser --session default --cdp 9222 tab
```

## Windows Troubleshooting Quick Map

- Symptom: `Daemon failed to start (port: 127.0.0.1:<port>)` on first command.
  Likely checks: `AGENT_BROWSER_HOME` is set and points to the installed
  `agent-browser` package.
- Symptom: `session list` does not show expected sessions. Likely checks:
  current `AGENT_BROWSER_SOCKET_DIR` matches the one used when those sessions
  were started.
- In PowerShell, `@` is a special character, so if you want to interact with any
  elements that include `@`, warp them into quotes.

## Example Commands

```powershell
agent-browser --cdp 9222 tab
```

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="$env:TEMP\agent-browser-sock"
agent-browser --session ab10 --cdp 9222 snapshot -i
```
