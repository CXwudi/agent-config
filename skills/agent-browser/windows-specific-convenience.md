
# Windows Specific Convenience

You must follow these:

## 1. Always set `AGENT_BROWSER_HOME` to avoid the `\\?\` path issue

Set `AGENT_BROWSER_HOME` to the installed `agent-browser` package root

If you installed `agent-browser` with pnpm, ask pnpm for its global modules
directory and resolve `agent-browser` from there. This works even if pnpm is
configured under a custom directory or on a different drive.

```powershell
$agentBrowserHome = (Resolve-Path (Join-Path (pnpm root -g) "agent-browser")).Path
$env:AGENT_BROWSER_HOME = $agentBrowserHome
```

Use the same package manager that installed `agent-browser`. For a pnpm global
install, prefer `pnpm root -g` over `npm root -g`.

Required check:

```powershell
Test-Path (Join-Path $env:AGENT_BROWSER_HOME "dist\daemon.js")
```

## 2. Choose session names that map to unblocked ports

Run:

```powershell
netsh interface ipv4 show excludedportrange protocol=tcp
```

To get all ports reserved by Windows.

Pick a session name whose port does not fall within any excluded range.
First check if default session name `default` works.

Calculate the port for a session name with Node.js:

```powershell
function Get-SessionPort($name) {
  node -e 'const name = process.argv[1]; let hash = 0; for (const c of name) { hash = ((hash << 5) - hash + c.charCodeAt(0)) | 0; } console.log(49152 + (Math.abs(hash) % 16383));' $name
}
```

If the calculated port ever looks wrong, check the upstream
`get_port_for_session` implementation in
[`cli/src/connection.rs`](https://github.com/vercel-labs/agent-browser/blob/main/cli/src/connection.rs).

## 3. Use writable socket directory only if needed

`~/.agent-browser` should be writable by default. If you hit socket dir
visibility or cleanup issues, set a known writable directory:

```powershell
$env:AGENT_BROWSER_SOCKET_DIR="C:\path\to\writable\agent-browser-sock"
```

## 4. Keep `AGENT_BROWSER_SOCKET_DIR` consistent per workflow

`AGENT_BROWSER_SOCKET_DIR` affects where session metadata (`*.pid`, `*.port`) is
stored. If you switch this value between commands, `session list` may not show
sessions started under the other directory.

Pick one strategy for the whole workflow:

- leave it unset to use `~/.agent-browser`
- set a custom directory once and reuse it for every command

## 5. Bootstrap environment once before first command (Windows)

On this Windows machine, `AGENT_BROWSER_HOME` is required for reliable daemon
cold-start. Set it before the first `agent-browser` command in a shell.

```powershell
$env:AGENT_BROWSER_HOME = (Resolve-Path (Join-Path (pnpm root -g) "agent-browser")).Path
# Optional. If you set this, keep it consistent for the whole workflow.
# $env:AGENT_BROWSER_SOCKET_DIR="C:\Users\11134\AppData\Local\Temp\agent-browser-sock"
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
$env:AGENT_BROWSER_HOME = (Resolve-Path (Join-Path (pnpm root -g) "agent-browser")).Path
agent-browser --cdp 9222 tab
```

```powershell
$env:AGENT_BROWSER_HOME = (Resolve-Path (Join-Path (pnpm root -g) "agent-browser")).Path
$env:AGENT_BROWSER_SOCKET_DIR="C:\path\to\writable\agent-browser-sock"
agent-browser --session ab10 --cdp 9222 snapshot -i
```

```powershell
Get-SessionPort "ab10"
```
