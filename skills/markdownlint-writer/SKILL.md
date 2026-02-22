---
name: markdownlint-writer
description: Agent Skill for markdownlint-compliant Markdown. Use after creating or editing Markdown.
---

# Markdownlint Writer

## Workflow

1. Identify the Markdown file(s) being created or edited.
1. Run `markdownlint-cli2` after every Markdown change on the modified file(s).
1. And learn from the linter's feedback to improve your Markdown writing skills over time.

## Lint Command

Run the linter on the exact files you changed.

```sh
markdownlint-cli2 "README.md" "docs/guide.md"
```

If the tool is unavailable or fails unexpectedly, tell the user and request
guidance.

## Checklist Of Common Rules

- `MD001` Heading levels should only increment by one.
- `MD003` Use a consistent heading style.
- `MD007` Use consistent list indentation.
- `MD009` No trailing spaces.
- `MD010` No hard tabs, use spaces.
- `MD012` Avoid multiple consecutive blank lines.
- `MD022` Add blank lines around headings.
- `MD025` Use a single H1 per file.
- `MD029` Use consistent ordered list numbering.
- `MD030` Use consistent spacing after list markers.
- `MD032` Add blank lines around lists.
- `MD040` Fenced code blocks should specify a language.
- `MD041` File should start with a top-level heading if required.
- `MD042` No empty links like `[]()` or `[text]()`.
- `MD047` File should end with a single newline.

## Common AI Mistakes

This section is intentionally left blank for the user to fill in later.
