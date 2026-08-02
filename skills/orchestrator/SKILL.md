---
name: orchestrator
description: Agent Skill for entering orchestration mode. Use when the user want you to become an orchestrator of multiple subagents.
---

# Orchestration Mode

When entering the orchestration mode, you will become an orchestrator of multiple subagents.
You don't do the work yourself.
Instead, you let your subagents do the work for you.

## Common Patterns

Here are some sample common patterns of subagent.
But you are not restricted to these patterns. You can spawn any subagent for any purpose.

### Exploration Agent

You can spawn a subagent to explore the topic, whether it is for exploring code bases, searching internet, or anything that requires long exploration and research.

Prefer to use a model with 1M context window for exploration agent.

For the best of acknowledging the exploration results, tell the exploration agent to write the results in markdown files

### Coding Agent

As title, you can spawn a subagent to do coding works

### Code Review Agent

The most common pattern of subagent. Spawn a subagent to review the finished coding works.
Often the time the subagent with brand new context window, can better spot issues in the code.

Prefer to use a different model than the one used in the coding agent. Usually Gemini model is a good choice.
