---
name: context-recorder
description: Agent Skill for recording contexts in a proper, consistent format. Use in any situation where context is needed, such as creating a new chat session, handing a prompt to a new AI agent, compacting chat history, or preparing summaries and reports, and etc. The purpose of recording context is to avoid repeated exploration work between multiple agents/humans. This skill is usually invoked by other skills, commands or tasks, but user can also directly invoke this skill for other purposes.
---

# Contex Skill

## Format

To properly record a context, following the following format in markdown:

```markdown
## References
<!-- list of references, such as files, urls, or other resources -->

| Resouce | Description | Must Read or Not |
| --- | --- | --- |
| ![a file](path/to/file) | a brief description of the file | Must Read / Optional Read |
| [a url](https://example.com) | a brief description of the url | Must Read / Optional Read |
```

## Notes

- You can add anything before the format mentioned above, depends on the tasks.
    - For example, a prompt file may add a `## Prompt` section at the beginning
    - For example, a report or a plan file will have their own format, followed by the context format mentioned above.
- When referring a file, if such file is too large, and only specific sections are needed. You can use the format `<file-path>:<start-line>:<end-line>` to guide the AI Agent to read only the required section of such file to avoid context overflow.
    - You can refer to a file several times with different sections
