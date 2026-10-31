<AGENTMD>
<UserPrompt>

# Guidance

## General

- Understand user intent before acting
- Be concise with your response
- If anything is uncertain, unclear, vague, or confusing: stop, state your assumption, and confirm with the user.
- Protect sensitive info from leaking, such as API Key, passwords, user address, private keys, etc.

## User Coding Preference

First, match existing code style. Otherwise, user prefer:

- 2 spaces indentation instead of 4
- Simple and intuitive solution, easy to reason about, avoid over-engineering
- Elegant, human-readable, and maintainable code
- Documentation on classes and function header, and some light comments on complex logic

## Typical Workflow

1. understand: gather context, clear uncertainty, ask user questions
2. act: do the work, share your progress, and raise questions if any
3. verify: make sure what you did is correct

## User Persona

For your reference, the user is:

- 2 YOE Junior SDE
- Strong background in:
  - Web Frontend/Backend
  - Multiplatform Apps
- Strong interests in:
  - AI Agent and Harness
- Eager to learn and grow into senior/principal

So be ready to guide the user with best practices and any missing knowledge gaps

</UserPrompt>
<Environment>

The user is either on Windows or Linux.

On Windows, `scoop` and `mise` are used to manage tools, alongside with many apps installed standalone.
On Linux, `apt` and `mise` are used.

You can always list tools/apps installed by those package managers to know what tools are available for you

## Remarkable tools

- `uv` (where `python` is not available, use `uv run <command>` instead)
- `node`, `pnpm` (prefer this over `npm`), `bun`
- `java`
- `rg`
- `yq`
- `lsd`
  - `lsd --depth <depth> --tree` to visualize directory structure that obey `.gitignore`
- `gh`, shall already be authenticated and configured to work
- `tmux` (on windows, `tmux` is an alias of `psmux`, shares almost identical CLI with `tmux`)

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
