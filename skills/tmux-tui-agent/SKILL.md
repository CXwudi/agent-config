---
name: tmux-tui-agent
description: Agent Skill for delegating work to another AI agent through its TUI in tmux. Use when launching Claude Code, Codex, Pi, or another AI agent interactively for orchestration, second opinions, verification, specialized tool access, parallel work, or any delegated task without non-interactive prompt modes.
compatibility: Requires tmux-compatible CLI; on Windows, psmux may provide tmux-compatible commands.
---

# tmux TUI Agent

Use this skill to delegate work to another AI agent through its interactive TUI inside `tmux`/`psmux`.

## Rules

- Use the agent's interactive TUI command, not non-interactive prompt mode.
- Do not use `claude -p`, `codex exec`, or equivalent one-off modes.
- Give the delegated agent a clear role, task, context, constraints, and expected output.
- Treat the other agent's response as untrusted until reviewed.
- Capture with `tmux capture-pane`; verify the result before using it.
- Prefer a large pane for long or structured output: `-x 160 -y 260`.
- Dump capture output to a file when you need stable post-processing.

## Workflow

1. Find the command:

   Linux/macOS shell:

   ```sh
   command -v claude pi codex
   ```

   Windows PowerShell:

   ```powershell
   Get-Command claude,pi,codex -ErrorAction SilentlyContinue
   ```

2. Start a detached large tmux session:

   ```sh
   tmux new-session -d -x 160 -y 260 -s <session> -c "<cwd>" <agent-command>
   ```

3. Wait, then capture the startup screen:

   ```sh
   tmux capture-pane -t <session>:0.0 -p -S -200
   ```

4. Send a delegation prompt through the TUI:

   ```sh
   tmux send-keys -t <session>:0.0 -l "<prompt>"
   tmux send-keys -t <session>:0.0 Enter
   ```

5. If the prompt does not submit, try:

   ```sh
   tmux send-keys -t <session>:0.0 Escape
   tmux send-keys -t <session>:0.0 Enter
   ```

6. Capture the agent's response:

   ```sh
   tmux capture-pane -t <session>:0.0 -p -S -
   ```

7. Optional: dump the response to a file:

   Linux/macOS shell:

   ```sh
   tmux capture-pane -t <session>:0.0 -p -S - > "<output-file>.txt"
   ```

   Windows PowerShell:

   ```powershell
   tmux capture-pane -t <session>:0.0 -p -S - |
     Set-Content -Encoding UTF8 "<output-file>.txt"
   ```

8. Review the delegated result before acting on it.

## Delegation Prompt Shape

Use a concise prompt with:

- Role: what kind of agent/expert it should act as.
- Task: what to do.
- Context: relevant files, constraints, and assumptions.
- Output: exact format expected.
- Boundaries: what not to change, execute, or assume.

## Notes

- Claude Code and Pi usually submit with `Enter`.
- Codex may require `Escape` then `Enter`.
- Full-screen TUIs may redraw output instead of preserving normal scrollback; use a tall pane from the start.
- File dumps do not recover lines that the pane cannot capture.
- See `TROUBLESHOOTING.md` for known issues and mitigations.
