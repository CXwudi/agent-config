# Windows Specific Convenience

You must follow these to smoothly run `agent-browser` on Windows.

## 1. Choose session names that map to unblocked ports

First run:

```powershell
netsh interface ipv4 show excludedportrange protocol=tcp
```

To get all ports reserved by Windows.

To be able to pick a session name whose port does not fall within any excluded range.
You need the following Node.js script to calculate the port for a session name:

```powershell
function Get-SessionPort($name) {
  node -e 'const name = process.argv[1]; let hash = 0; for (const c of name) { hash = ((hash << 5) - hash + c.charCodeAt(0)) | 0; } console.log(49152 + (Math.abs(hash) % 16383));' $name
}
```

> If the calculated port ever looks wrong, check the upstream
> `get_port_for_session` implementation in
> [`cli/src/connection.rs`](https://github.com/vercel-labs/agent-browser/blob/main/cli/src/connection.rs).

First check if default session name `default` maps to an unblocked port.
If not, try out a few different session names until you find one that maps to an unblocked port.

## 2. Use writable socket directory only if needed

In a normal local shell, `~/.agent-browser` is usually writable. In sandboxed
environments such as Codex, it may not be. If you hit socket dir visibility,
cleanup, or write-permission issues, set a known writable directory:

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="$env:TEMP\agent-browser-sock"
```

## 3. Keep `AGENT_BROWSER_SOCKET_DIR` consistent per workflow

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
- Symptom: `Daemon failed to start (port: 127.0.0.1:<port>)` for one session
  name but not others.
  Likely checks: mapped session port is excluded by Windows.
- Symptom: `session list` does not show expected sessions.
  Likely checks: current `AGENT_BROWSER_SOCKET_DIR` matches the one used when
  those sessions were started.

## Example Commands

```powershell
agent-browser --cdp 9222 tab
```

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="$env:TEMP\agent-browser-sock"
agent-browser --session ab10 --cdp 9222 snapshot -i
```

```powershell
Get-SessionPort "ab10"
```
