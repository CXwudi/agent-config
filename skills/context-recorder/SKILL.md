---
name: context-recorder
description: Agent Skill for recording contexts in a proper, consistent format. Use in any situation where context is needed, such as creating a new chat session, handing a prompt to a new AI agent, compacting chat history, or preparing summaries and reports, and etc. The purpose of recording context is to avoid repeated exploration work between multiple agents/humans. This skill is usually invoked by other skills, commands or tasks, but user can also directly invoke this skill for other purposes.
---

# Contex Skill

## Format

To properly record a context, following the following format in markdown:

```markdown
## References

### Must Read

<!-- one or several markdown table listing key files (usually key source files, key documentation) that AI Agents must read -->

### Optional Read

<!-- one or several markdown table that AI Agents can optionally read -->
<!-- this section can also be used to refer other contexts files -->

## Contexts

<!-- Any context information not mentioned in the references above, be precise and clear, do not duplicate with references above -->
```

## Notes

- You can add anything before the format mentioned above, depends on the tasks.
    - For example, a prompt file may add a `## Prompt` section at the beginning
    - For example, a report or a plan file will have their own format, followed by the context format mentioned above.
- When referring a file, if such file is too large, you can use the github format `<file-path>#L<start-line>-L<end-line>` to refer to a specific section of the file, to guide the AI Agent to read only the required section of such file to avoid context overflow.
