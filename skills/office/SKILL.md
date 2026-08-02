---
name: office
description: Agent Skill for Word, Excel, PowerPoint, and other office works.
---

# Office

You have two options to do office works:

1. Load `python` skill and write code that utilizes various python libraries to do the office works.
2. Use OfficeCLI

# OfficeCLI

## Prerequisites

`officecli` command is available in `$PATH`

## Usage

Run `officecli --help` to see the usage and available commands.

And navigate to `https://raw.githubusercontent.com/iOfficeAI/OfficeCLI/refs/heads/main/SKILL.md` for detailed guidance.

## Note

- Sometime when running `officecli` command, it may generate a new Agent Skill file with `officecli` name into various agent. Look for some logs like below:

  ```
    Claude Code: officecli installed (C:\Users\<USER>\.claude\skills\officecli\SKILL.md)
    GitHub Copilot: officecli installed (C:\Users\<USER>\.copilot\skills\officecli\SKILL.md)
    Codex CLI: officecli installed (C:\Users\<USER>\.agents\skills\officecli\SKILL.md)
    Pi: officecli installed (C:\Users\<USER>\.pi\agent\skills\officecli\SKILL.md)
    OpenCode: officecli installed (C:\Users\<USER>\.config\opencode\skills\officecli\SKILL.md)
  Registered officecli MCP in VS Code Copilot.
    Config: C:\Users\<USER>\.vscode\mcp.json
  ```

  If this log is found, IMMEDIATELY delete these generated `officecli` skill files, and clean up the `mcp.json` file. Failing to do so will cause conflicts with this current `office` skill.

