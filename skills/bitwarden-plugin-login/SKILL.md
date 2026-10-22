---
name: bitwarden-plugin-login
description: Agent Skill for safely logging into using Bitwarden browser extension. Use when you want to login to a website or account on behalf of the user
---
# Bitwarden Plugin Login

## Prerequisites

1. Load the `use-browser` skill, or have Computer Use ready
2. `BITWARDEN_PIN` environment variable is available

## Workflow

Open the browser, and open the Bitwarden extension, unlock it using the PIN from `BITWARDEN_PIN`.
If you can not unlock it using the PIN, stop and report it back to the user. Do not use master password to login to bitwarden.

Then when you login to a website or an account, you should be able to login using the Bitwarden extension

## Notes

- Absolute no for revealing the password in the chat.
- So far no login for finance related accounts (e.g. bank accounts, investment accounts). Ask for user confirmation before you do so.
