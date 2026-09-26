---
name: opencli
description: Agent Skill for browser automation via OpenCLI and its browser bridge plugin.
compatibility: Requires the OpenCLI command `opencli`.
---

# OpenCLI

OpenCLI for browser automation.

## Prerequisites

1. `opencli` is available in the `$PATH`.
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

Discover the current CLI surface from help output:

```sh
opencli browser --help
```

Prefer `-f yaml` or `-f json` when available so command arguments, options, access level, browser requirements, and output columns are structured.

We are not using any OpenCLI adapters in this skill, do not use OpenCLI adapters unless user told you to use so.

## Common Workflows

1. Make sure `opencli doctor` runs successfully once before proceeding.
1. Read `opencli browser --help` and the relevant subcommand help.
1. Pick a descriptive browser session name and reuse it across related calls.
1. Use `opencli browser <session> state` to inspect interactive element indices before clicking, typing, selecting, uploading, or dragging.


## Safety Rules

- Confirm with the user before commands that log in, post, send, purchase, subscribe, create, update, delete, upload, download private data, change profile/session defaults, install/uninstall plugins, or control daemon lifecycle.
- Do not print secrets, tokens, cookies, credentials, session exports, or private browser data. Summarize only what the task requires.
- If a command fails because OpenCLI's daemon, extension, profile, or browser session is not ready, report the specific failed check and the next user-visible setup step.
