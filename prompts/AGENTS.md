# Guidance

## General

- prefer 2 spaces indentation instead of 4
- follow existing conventions (naming, formatting, structure, tone, templates) before introducing new patterns
- avoid large change in one go, apply changes incrementally
- when unsure or unclear about something, ask the user for clarification (more details below)
- about documentation, at least functions and classes should be documented
- about comments, focus on why (tradeoffs, constraints), not what; do not “talk to the user” through comments

### About asking for clarification

You should always proactively ask for clarification whenever you find something unclear, missing, or even conflicting with user requests.

During planning or implementing, you can always pause at the middle and ask for clarification, before you move on.

## Terminal Tools

Prefer these terminal tools over any tools that provide similar functionalities.
All these tools are installed and safe to execute:

- `ast-grep` to search for symbols/snippets in source code based on abstract syntax tree, prefer this over regex-based search tools for code searching
- `tre` to list files and directories (use `tre -l <depth>` to limit depth of the tree), replacement for `tree`
- `rg` to search for text in files
- `yq` to process JSON, YAML, and XML files
- `lsd` to list files and directories, replacement for `ls`

Notes:

- On windows, if some commands failed to run, try using `powershell -Command "<command>"` to run them.

## Typical Workflow

1. understand: gather context, inspect patterns and conventions; never assume, always verify with evidence
2. plan: plan your approach with incremental steps; verify your plan with the user
3. implement: incrementally based on the plan, consistent with conventions and patterns; ask for clarification whenever needed
4. verify: if applicable, verify the changes with tests
