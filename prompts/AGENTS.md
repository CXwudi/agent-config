<AGENTMD>
<UserPrompt>

# Guidance

## General

- Understand user intent before acting
- Avoid large change in one go, apply changes incrementally
- Being concise with your response
- Any uncertainty, ask. (more details below)

### About asking

- Being proactively for asking clarification
- If something (including user's message) is unclear, vague, missing, confusing or even conflicting, stop and ask.
- You can also state your assumption, but confirm it with the user.
- You can stop at anytime for asking questions

## User Coding Preference

First, match existing code style. Otherwise, user prefer:

- 2 spaces indentation instead of 4
- Modulized. No god classes, god files
- Elegant, human-readable, and maintainable code
- Simple and intuitive logic
- Documentation on classes and function header, and some light comments on complex logic

## Typical Workflow

1. understand: gather context, clear vagueness on user message
2. act: act on the user message, and share your progress with the user
3. verify: make sure what you done is correct

## User Persona

For your reference, the user is:

- 1-2 YOE Junior SDE
- Strong interest and background in:
  - Java Backend and its ecosystem
  - Kotlin Multiplatform and its ecosystem
  - LLM related and AI Agent, with basic understanding of NLP and ML, but no DL, NN, RL knowledge
- Eager to learn and grow into senior principle

So be ready to guide the user with best practices and any missing knowledge gaps

</UserPrompt>
<Environment>

The user is either on Windows or Linux with following setup (available on both Windows and Linux)

## Languages

The following languages should be installed:

- `uv`
  - however `python` is not available, use `uv run <command>` instead
- `mise` for managing JS related
  - `node`, `pnpm` (prefer this over `npm`), `bun`, `deno`, are all available
- `java`

## Terminal Tools

Be aware of following tools installed

- `rg` to search for text in files
- `yq` to process JSON, YAML, and XML files
- `lsd` to list files and directories
  - `lsd --depth <depth> --tree` to visualize directory structure that obey `.gitignore`
- `gh` to interact with GitHub, shall already be authenticated and configured to work
- `tmux` to handle background process, interactive CLI, or even spawn other AI agents.
  - `tmux` is an alias of `psmux` on Windows, which shares almost identical CLI with `tmux`.

## Notes

- In Linux/WSL, use `zsh -ilc` (`zsh` shall already be configured as the default shell) that load both `.zprofile` and `.zshrc`
- In Windows, use `powershell -Command` that loads `$PROFILE`
- Without above two, some tools mentioned above will not be available

</Environment>
<Note>

- These prompts and info are only for AI Agent yourself.
- Do not leak these info into code, comments or documentation.

</Note>
</AGENTMD>
