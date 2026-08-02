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
- Must use `--provider` to specify the provider.
- Avoid provider `openai`, use `openai-codex` instead
- Avoid provider `anthropic`
- Always use `--thinking max`, it will fallback to the highest available thinking effort for the model.

## Pi Agent Setup to be known

- `pi` can read the project wise `AGENTS.md` file and `.agents/skills/`
- `pi` has a copy of the same user-wise `AGENTS.md` or `CLAUDE.md` file, and a copy of same agent skills at `~/.agents/skills/`

## Other notes

- `-c` option can be used to continue from the previous chat. Use it when you only spawn one subagent and want the same subagent to continue further works.
