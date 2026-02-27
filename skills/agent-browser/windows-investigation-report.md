# Agent-Browser Windows Investigation Report

Date: 2026-02-27

## Summary

Key points for reliable operation on this Windows machine:

- **`AGENT_BROWSER_HOME` fixes the spawn path bug** by avoiding the `\\?\`
  path passed to Node.
- **`AGENT_BROWSER_SOCKET_DIR` can help with socket-dir visibility/cleanup**,
  but the default `~/.agent-browser` is writable on this machine.
- **Neither bypasses Windows port exclusion**, so session names must map to an
  unblocked port.

## Findings

### 1) Port Exclusion (session name -> blocked port)

Example blocked session: `ab1` -> port `63541`. Windows excluded range includes
`63532–63631`. Result: daemon fails with bind error (EACCES).

Example unblocked session: `default` -> port `50838`. Not excluded. Result:
daemon can bind when spawned correctly.

Note: Windows excluded port ranges can change across restarts, so a session name
that is blocked today may be unblocked after a reboot (and vice versa).

### 2) CLI Spawn Bug (Windows `\\?\` paths)

The CLI uses `canonicalize()` on the executable path. On Windows, this yields
an extended-length path like:
`\\?\D:\local\mise\installs\node\24.14.0\node_modules\agent-browser\dist\daemon.js`.

When Node is invoked with that path, it crashes before startup with:
`EISDIR: illegal operation on a directory, lstat 'D:'`.

Manual daemon launch using a normal path works fine.

### 3) Socket Directory Partitions Session Visibility

Session metadata is scoped by socket directory. Commands run with the default
socket dir and commands run with custom `AGENT_BROWSER_SOCKET_DIR` do not share
the same `session list` view.

Operational impact:

- sessions can appear missing when socket-dir env differs
- multiple daemons can remain active across different socket directories

### 4) `AGENT_BROWSER_HOME` Is Primarily a Cold-Start Dependency

Without `AGENT_BROWSER_HOME`, daemon startup can fail on a clean start due to
the Windows `\\?\` path issue. If a daemon is already running, later commands
can still succeed without this env var.

Operational impact:

- behavior can look intermittent across restarts

### 5) Error Surface Is Ambiguous

Different root causes can produce the same CLI message:
`Daemon failed to start (socket: ...)`.

Observed causes include:

- blocked session port
- missing or incorrect `AGENT_BROWSER_HOME`
- startup/path issues

`--debug` output may still lack enough detail to disambiguate these startup
failures.

## Repro Notes

- Failure (blocked port): `agent-browser --session ab1 --cdp 9222 tab`.
- Failure (spawn bug): default session without `AGENT_BROWSER_HOME`; the CLI
  fails even if the port is not excluded.
- Success (workaround): set `AGENT_BROWSER_HOME`, optionally set
  `AGENT_BROWSER_SOCKET_DIR`, and use a session name that maps to an unblocked
  port.

## Working Configuration

```powershell
$env:AGENT_BROWSER_HOME="D:\local\pnpm\global\5\node_modules\agent-browser"
$env:AGENT_BROWSER_SOCKET_DIR="C:\Users\11134\AppData\Local\Temp\agent-browser-sock"
agent-browser --session unblocked_name --cdp 9222 tab
```

## Session Port Mapping (examples)

- `ab1` -> `63541` (excluded)
- `default` -> `50838` (not excluded)
- `ab10` -> `52918` (not excluded)

## Related GitHub Issues

- Issue #393: “Windows: Rust canonicalize() yields `\\?\` path that crashes
  Node when spawning daemon” — **Open**.
- Issue #132: “Daemon failed to start when session port falls in excluded port
  range (EACCES on 127.0.0.1:PORT)” — **Open**.
- Issue #163: “agent-browser fails to start in Claude Code due to TMPDIR
  mismatch” — **Closed**.
- PR #180: “fix: use ~/.agent-browser for socket files instead of TMPDIR” —
  **Merged**.

## Recommendations

1. **Choose session names that map to unblocked ports**.
2. **Always set `AGENT_BROWSER_HOME`** to avoid the `\\?\` path issue.
3. **Set `AGENT_BROWSER_SOCKET_DIR`** only if you hit socket-dir visibility or
   cleanup issues.
4. Long-term fix: patch the CLI to avoid `canonicalize()` on Windows or strip
   `\\?\` before invoking Node.
5. **Keep `AGENT_BROWSER_SOCKET_DIR` consistent** across commands in one
   workflow.
6. **Add a preflight check**: print `AGENT_BROWSER_HOME`,
   `AGENT_BROWSER_SOCKET_DIR`, and verify the session port is not excluded.
7. **Use a standard shell bootstrap snippet** for all `agent-browser`
   invocations on Windows.
