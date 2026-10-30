---
name: use-browser
description: Agent Skill for using a browser. Use when browser access is needed
---

# Use Browser

This is a combination of 2 skills:

- [`opencli`](./opencli/SKILL.md)
- [`agent-browser`](./agent-browser/SKILL.md)

When to use which:

1. `opencli`:
    - Your default choice
    - Robust automation
    - Reuse existing user profile and session
1. `agent-browser` for:
    - Web development, testing, and debugging

## Notes

- Open the browser with the existing user's profile, to reuse the existing session and cookies, and persist new sessions for future use by AI Agents and user. No new profile, no temp profile, no clone of a profile.
- Both are capable for reusing user's existing browser session, tho `opencli` is more preferred.
