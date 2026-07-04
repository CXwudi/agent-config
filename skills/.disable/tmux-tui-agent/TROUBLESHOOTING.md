# tmux TUI Agent Troubleshooting

## psmux cannot create a session

Symptom:

```text
psmux: failed to create session '<name>'
```

Mitigation:

- Retry with elevated/unsandboxed command permission if the environment requires it.
- Keep the command scoped, for example `tmux new-session ...`.

## Prompt appears but does not submit

Observed with Codex.

Mitigation:

```sh
tmux send-keys -t <session>:0.0 Escape
tmux send-keys -t <session>:0.0 Enter
```

Avoid sending literal `Return`; it may type the word `Return` into the prompt.

## Only the last lines are captured

Symptom:

- Agent outputs long content.
- `capture-pane` only sees the visible tail.
- Dumping `capture-pane` output to a file still only saves those visible/capturable lines.

Cause:

- Some TUIs render like full-screen apps and do not preserve all output as normal terminal scrollback.

Mitigation:

- Start the session with enough visible height before generating output:

  ```sh
  tmux new-session -d -x 160 -y 260 -s <session> -c "<cwd>" <agent-command>
  ```

- Then capture all visible content:

  ```sh
  tmux capture-pane -t <session>:0.0 -p -S -
  ```

- For stable later parsing, dump the capture output to a file:

  Linux/macOS shell:

  ```sh
  tmux capture-pane -t <session>:0.0 -p -S - > "<output-file>.txt"
  ```

  Windows PowerShell:

  ```powershell
  tmux capture-pane -t <session>:0.0 -p -S - |
    Set-Content -Encoding UTF8 "<output-file>.txt"
  ```

## First output line has a bullet

Symptom:

```text
• <agent output>
● <agent output>
```

Mitigation:

- Use a regex that tolerates TUI decorations:

  ```powershell
  '^\s*[•●]?\s*(?<content>.*)$'
  ```

## Validation example: 200-line capture test

To test whether an agent TUI can be fully captured, ask it to output exactly 200 numbered lines, then parse the result:

Linux/macOS:

```sh
tmux capture-pane -t <session>:0.0 -p -S - > capture.txt
seq -f 'LINE %03g' 1 200 |
  while IFS= read -r line; do
    grep -Eq "^[[:space:]]*[•●]?[[:space:]]*$line[[:space:]]*$" capture.txt ||
      echo "missing: $line"
  done
```

Windows PowerShell:

```powershell
$lines = tmux capture-pane -t <session>:0.0 -p -S -
$nums = foreach ($line in $lines) {
  if ($line -match '^\s*[•●]?\s*LINE (\d{3})\s*$') { [int]$Matches[1] }
}
$missing = 1..200 | Where-Object { $_ -notin $nums }
[pscustomobject]@{
  Count = $nums.Count
  First = $nums | Select-Object -First 1
  Last = $nums | Select-Object -Last 1
  Missing = $missing -join ','
} | Format-List
```

## Modified Enter keys may not work

Observed warning in Pi:

```text
tmux extended-keys is off
```

Mitigation:

- Normal `Enter` still worked in the test.
- If modified Enter keys are required, add this to tmux config and restart tmux:

  ```text
  set -g extended-keys on
  ```

## Practical verification result

Tested successfully:

- Claude Code TUI: captured 200/200 lines.
- Pi Coding Agent TUI: captured 200/200 lines.
- Codex TUI: captured 200/200 only after using a tall `160x260` pane.
