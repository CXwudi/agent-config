---
name: context-skill
description: Agent Skill for recording contexts in a proper, consistent format. Use in any situation where context is needed, such as creating a new chat session, handing a prompt to a new AI agent, compacting chat history, or preparing summaries and reports that benefit from context, and etc. This skill is usually invoked by other skills, commands or tasks, but user can also directly invoke this skill.
---

# Contex Skill

## Format

To properly record a context, following the following format in markdown:

```markdown
<!-- This section only lists references that an AI Agent should knows -->
## References

### Must Read

<!-- one or several markdown table that AI Agents must read -->

### Optional Read

<!-- one or several markdown table that AI Agents can optionally read -->

## Contexts

<!-- Any context information not mentioned in the references above, be precise and clear, do not duplicate with references above -->
```

## Notes

- Contexts can be recorded in a new markdown file, or appended at the end of an existing markdown file. Depends on the task.
