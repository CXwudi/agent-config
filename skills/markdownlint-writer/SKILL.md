---
name: markdownlint-writer
description: Agent Skill for markdownlint-compliant Markdown. Use after creating or editing Markdown.
---

# Markdownlint Writer

## Workflow

1. Identify the Markdown file(s) being created or edited.
1. Run `deno fmt` on the modified Markdown file(s) first.
1. Run `markdownlint-cli2 --fix` after formatting on the same file(s).
1. Use these tools to auto-format Markdown before relying on LLM-written edits
   for style-only cleanup.
1. Learn from formatter and linter feedback to improve your Markdown writing
   skills over time.

## Format And Lint Commands

Run the formatter and linter on the exact Markdown files you changed, in this
order:

```sh
deno fmt "README.md" "docs/guide.md"
markdownlint-cli2 --fix "README.md" "docs/guide.md"
```

If either tool is unavailable or fails unexpectedly, tell the user and request
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

## User Convention and Common AI Mistakes

1. Avoid extensive use of bolding.
2. Do not use bolding as a header. Use proper Markdown headings instead.
3. Usually a code block is fenced inside a triple backtick. But for code blocks
   of Markdown, use 4 backticks instead of 3.
