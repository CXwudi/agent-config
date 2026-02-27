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

### Windows Specific Convenience

#### 1. Choose session names that map to unblocked ports

Run:

```powershell
netsh interface ipv4 show excludedportrange protocol=tcp
```

To get all ports reserved by Windows.

Pick a session name whose port does not fall within any excluded range.
First check if default session name `default` works.

Calculate the port for a session name (PowerShell):

```powershell
function Get-SessionPort($name) {
  $hash = 0
  $name.ToCharArray() | ForEach-Object {
    $hash = (($hash -shl 5) - $hash + [int][char]$_)
    $hash = [int]$hash
  }
  49152 + ([math]::Abs($hash) % 16383)
}
```

#### 2. Always set `AGENT_BROWSER_HOME` to avoid the `\\?\` path issue

Set `AGENT_BROWSER_HOME` to the installed `agent-browser` package root

Example (pnpm global install):

```powershell
$env:AGENT_BROWSER_HOME="C:\path\to\pnpm\global\node_modules\agent-browser"
```

#### 3. Use writable socket directory only if needed

`~/.agent-browser` should be writable by default. If you hit socket dir
visibility or cleanup issues, set a known writable directory:

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="C:\path\to\writable\agent-browser-sock"
```

#### 4. Keep `AGENT_BROWSER_SOCKET_DIR` consistent per workflow

`AGENT_BROWSER_SOCKET_DIR` affects where session metadata (`*.pid`, `*.port`) is
stored. If you switch this value between commands, `session list` may not show
sessions started under the other directory.

Pick one strategy for the whole workflow:

- leave it unset to use `~/.agent-browser`
- set a custom directory once and reuse it for every command

#### 5. Bootstrap environment once before first command (Windows)

On this Windows machine, `AGENT_BROWSER_HOME` is required for reliable daemon
cold-start. Set it before the first `agent-browser` command in a shell.

```powershell
$env:AGENT_BROWSER_HOME="D:\local\pnpm\global\5\node_modules\agent-browser"
# Optional. If you set this, keep it consistent for the whole workflow.
# $env:AGENT_BROWSER_SOCKET_DIR="C:\Users\11134\AppData\Local\Temp\agent-browser-sock"
agent-browser --session default --cdp 9222 tab
```

#### Windows Troubleshooting Quick Map

- Symptom: `Daemon failed to start (socket: ...default.sock)` on first command.
  Likely checks: `AGENT_BROWSER_HOME` is set and points to the installed
  `agent-browser` package.
- Symptom: `Daemon failed to start (socket: ...<session>.sock)` for one session
  name.
  Likely checks: mapped session port is excluded by Windows.
- Symptom: `session list` does not show expected sessions.
  Likely checks: current `AGENT_BROWSER_SOCKET_DIR` matches the one used when
  those sessions were started.

#### Example Commands

```powershell
$env:AGENT_BROWSER_HOME="C:\path\to\pnpm\global\node_modules\agent-browser"
agent-browser --cdp 9222 tab
```

```powershell
$env:AGENT_BROWSER_HOME="C:\path\to\pnpm\global\node_modules\agent-browser"
$env:AGENT_BROWSER_SOCKET_DIR="C:\path\to\writable\agent-browser-sock"
agent-browser --session ab10 --cdp 9222 snapshot -i
```

```powershell
Get-SessionPort "ab10"
```
