---
name: use-computer
description: Agent Skill for controlling the current computer via GUI. Use when you need the full control. Also use it as the ultimate fallback to get any task done
---

# Use Computer

## Decision

Check the OS:

- on Windows, use [`cua`](cua/SKILL.md) skill.
- on Linux, check if GUI is available
  - if yes, simply just use whatever tool available to control the current GUI, e.g. `xdotool`, etc.
    - If no relevant tool, you can suggest user to allow you to install one.
  - otherwise, no GUI, just use terminal tool
