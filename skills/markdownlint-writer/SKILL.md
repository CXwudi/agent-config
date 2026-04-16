---
name: markdownlint-writer
description: Agent Skill for finalizing markdownlint-compliant Markdown. Use before git commit, when the user indicates the task is done, when you complete a meaningful phase of work, or when the user explicitly requests Markdown cleanup.
---

# Markdownlint Writer

## Workflow

1. Identify the Markdown file(s) created or edited during the current task or
   phase of work.
1. Do not run formatting or lint autofixes after every small Markdown edit. Keep
   drafting and iterative edits flexible until a finalization checkpoint.
1. Treat the following as finalization checkpoints:
   - Before `git commit`
   - When the user indicates the task is done
   - When you complete a meaningful phase of work
   - When the user explicitly asks for Markdown formatting or lint cleanup
1. At a finalization checkpoint, run `deno fmt` and `markdownlint-cli2 --fix` on
   the modified Markdown file(s).
1. Use these tools for final cleanup before relying on LLM-written edits for
   style-only fixes.
1. Learn from formatter and linter feedback to improve your Markdown writing
   habits over time.

## Format And Lint Commands

At a finalization checkpoint, run the formatter and linter on the exact Markdown
files you changed, in this order:

```sh
deno fmt "README.md" "docs/guide.md"
markdownlint-cli2 --fix "README.md" "docs/guide.md"
```

If either tool is unavailable or fails unexpectedly, tell the user and request
guidance.

If you are still in the middle of iterative drafting or ongoing work, defer
these commands until the current work is finalized.

## User Convention on Markdown format

1. Avoid extensive use of bolding.
2. Do not use bolding as a header. Use proper Markdown headings instead.
3. Usually a code block is fenced inside a triple backtick. But for code blocks
   of Markdown, use 4 backticks instead of 3.
