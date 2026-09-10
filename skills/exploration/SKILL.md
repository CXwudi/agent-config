---
name: exploration
description: Agent Skill for exploring the directory. Use when gathering context from local files
---

# Exploration

This is a combination of 2 skills:

- [ast-outline](ast-outline/SKILL.md)
- [ast-grep](ast-grep/SKILL.md)

When to use which:

- `ast-outline` for:
    - Checking the outline of a file or a directory, in a token efficient way
- `ast-grep` for:
    - Syntax-aware code search using `ast-grep`

## Note

- Don't just limit yourself to `tree`, `ripgrep` and other typical linux commands when exploring the repo or gathering context, be aware of the above tools and proactively use them to save tokens and context windows.
- You should always design your approach to gather context in a token efficient way.
