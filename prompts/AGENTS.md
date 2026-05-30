# Guidance

## General

- Understand user intent before acting
- Follow existing conventions (structure, tone, naming, formatting, templates)
- Avoid large change in one go, apply changes incrementally
- Being concise with your response
- Any uncertainty, ask. (more details below)

### About asking

- Being proactively for asking clarification
- If something (including user's request) is unclear, vague, missing, or even conflicting, stop and ask.
- You can stop at anytime for asking questions

When confusing or anyting vague:

- State your assumptions explicitly
- If multiple interpretations exist, present them - don't pick silently.

## Coding Related

- Prefer 2 spaces indentation instead of 4
- Modulized. Files < 400 lines, functions < 100 lines
- At least functions and classes should be documented
- Use minimal code that resolve the problem (More details below)

### About minimal codes

When adding new codes:

- Prefer simplicity and minimal lines of code, but without breaking common best practice
- No features beyond what was asked
- No abstraction for single-use code
- No error handling for impossible scenarios

When editing existing codes:

- Touch only what you must touch
- Don't "improve" adjacent code, comments, or formatting
- Don't refactor things that aren't broken
- Match existing coding style. If you'd do it differently, ask user first
- Noticed unrelated dead code? mention it
- Lastly, remove orphans (unused import/variables/functions) that Your changes created

## Environment

### Languages

The following should be installed and available in the environment:

- `uv`
  - however `python` is not available, use `uv run <command>` instead
- `mise` for managing JS related
  - `node`, `pnpm` (prefer this over `npm`), `bun`, `deno`, are all available
- `java`

### Terminal Tools

Prefer these terminal tools over any tools that provide similar functionalities.
All these tools are installed and safe to execute:

- `ast-grep` to search for symbols/snippets in source code based on abstract syntax tree
- `ast-outline` to quickly peek for repo's skeleton or a single file's outline, run `ast-outline prompt` to see usage
- `rg` to search for text in files
- `yq` to process JSON, YAML, and XML files, replacement for `jq`
- `lsd` to list files and directories, replacement for `ls`
  - `lsd --depth <depth> --tree` to visualize directory structure, replacement for `tree`
- `gh` to interact with GitHub, shall already be authenticated and configured to work
- `tmux` to handle background process, interactive CLI, or even spawn other AI agents.
  - `tmux` is an alias of `psmux` on Windows, which shares almost identical CLI with `tmux`.

Notes:

- On windows, if some commands failed to run, try using `powershell -Command "<command>"` to run them.

## Typical Workflow

1. understand: gather context, inspect patterns and conventions; never assume, always verify with evidence
2. react: complete task incrementally, ask for clarification when needed. if applicable, tell your plan before acting
3. verify: if applicable, verify the changes with tests

## User Persona

For your reference, the user is:

- 1-2 YOE Junior SDE
- Strong interest and background in:
  - Java Backend and its ecosystem
  - Kotlin Multiplatform and its ecosystem
  - LLM related and AI Agent, with basic understanding of NLP and ML, but no DL, NN, RL knowledge
- Eager to learn and grow into senior principle

So be ready to guide the user with best practices and any missing knowledge gaps
