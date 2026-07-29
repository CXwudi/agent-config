---
name: pi-subagent
description: Agent Skill for spawning a subagent via Pi Coding Agent. Use when spawning a subagent with different models, or to save cost.
---

## Prerequites

`pi --help` resolves and returns the help menu

Otherwise stop and tell the user to install Pi Coding Agent

## Choosing Models

Run `pi --list-models` to see all available models (or `pi --list-models <provider>` to see models for a specific provider)

- If you don't know, by default choose `deepseek-v4-pro` from `deepseek` provider.
- Avoid `openai`, use `openai-codex` instead
- Avoid `anthropic`
- Must use `--provider` to specify the provider.

## Pi Agent Setup to be known

- `pi` can read the project wise `AGENTS.md` file
- `pi` has a copy of the same user-wise `AGENTS.md` or `CLAUDE.md` file
- `pi` has the same Agent Skills setup as shown in the project `.agents/skills/` or `~/.agents/skills/` folder
