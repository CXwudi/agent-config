---
name: reference-recorder
description: Agent Skill for recording references in a proper, consistent format. Use in any situation where listing references can be beneficial, such as creating a new chat session, handing a prompt to a new AI agent, compacting chat history, or preparing summaries and reports, and etc. The purpose of references is to provide a catalog of resources. This skill is usually invoked by other skills, commands or tasks, but user can also directly invoke this skill for other purposes.
---

# Reference Recorder Skill

## Format

To properly record references, following the following format in markdown:

```markdown
## References
<!-- list of references, such as files, urls, or other resources -->

| Resouce | Description | Other Notes if any |
| --- | --- | --- |
| ![a file](path/to/file) | a brief description of the file | |
| [a url](https://example.com) | a brief description of the url | |
```

## Notes

- You can add anything before the format mentioned above, depends on the tasks.
    - For example, a prompt file may add a `## Prompt` section at the beginning
    - For example, a report or a plan file will have their own format, followed by the context format mentioned above.
- When referring a file, if such file is too large, and only specific sections are needed. You can use the format `<file-path>:<start-line>:<end-line>` to guide the AI Agent to read only the required section of such file to avoid context overflow.
    - You can refer to a file several times with different sections
- Other Notes column is optional and can leave empty. However, for important files or urls, you can add "Must Read" or "Important" to make it stand out for AI Agents
