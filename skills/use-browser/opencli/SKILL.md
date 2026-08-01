---
name: opencli
description: Agent Skill for OpenCLI. Use when the user wants to control websites through the `opencli` CLI, run or inspect OpenCLI site/app/external adapters, use the OpenCLI browser bridge/CDP automation
compatibility: Requires the OpenCLI command `opencli`.
---

# OpenCLI

OpenCLI makes websites available as CLI commands through adapters and browser bridge automation.

## Prerequisites

1. The `opencli` binary must be on `$PATH`.
2. 
    ```sh
    opencli doctor
    ```
    If `opencli doctor` reports missing daemon, missing extension, or failed connectivity, summarize the failing checks. First try again without the sandbox (for codex). If still failed, report back to the user

    You may inspect daemon state when useful:

    ```sh
    opencli daemon status
    ```

## Command Discovery

Do not assume adapter names, command names, arguments, or flags. Discover the current CLI surface from help output:

```sh
opencli --help
opencli list -f yaml
opencli <site-or-adapter> --help -f yaml
opencli <site-or-adapter> <command> --help -f yaml
opencli browser --help
```

Prefer `-f yaml` or `-f json` when available so command arguments, options, access level, browser requirements, and output columns are structured.

## Common Workflows

For site/app/external adapters:

1. Use `opencli list -f yaml` to find relevant adapters.
1. Inspect the adapter with `opencli <adapter> --help -f yaml`.
1. Inspect the exact command with `opencli <adapter> <command> --help -f yaml`.
1. Choose output format intentionally, usually `-f yaml` or `-f json` for downstream reasoning.

For direct browser control:

1. Make sure `opencli doctor` runs successfully once before proceeding.
1. Read `opencli browser --help` and the relevant subcommand help.
1. Pick a descriptive browser session name and reuse it across related calls.
1. Use `opencli browser <session> state` to inspect interactive element indices before clicking, typing, selecting, uploading, or dragging.

For adapter development or verification:

```sh
opencli validate <target>
opencli verify <target>
opencli convention-audit <target>
```

Inspect each command's help before passing flags.

## Safety Rules

- Confirm with the user before commands that log in, post, send, purchase, subscribe, create, update, delete, upload, download private data, change profile/session defaults, install/uninstall plugins, or control daemon lifecycle.
- Do not print secrets, tokens, cookies, credentials, session exports, or private browser data. Summarize only what the task requires.
- If a command fails because OpenCLI's daemon, extension, profile, or browser session is not ready, report the specific failed check and the next user-visible setup step.
