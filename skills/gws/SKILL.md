---
name: gws
description: Agent Skill for Google Workspace CLI. Use when interacting with user's Gmail, Calendar, Drive, Sheets, Docs, Tasks, etc. Google Services.
---

# gws — Google Workspace CLI

## Prerequisites

The `gws` binary must be on `$PATH`.

### Authentication

Before accessing live Workspace data, first verify that the default OAuth client secret file exists:

```bash
test -f ~/.config/gws/client_secret.json
```

If `~/.config/gws/client_secret.json` is missing, ask the user to provide it before proceeding. 

When the client secret file is present, check authentication status:

```bash
gws auth status
```

Do not paste the full auth status output into chat due to security concerns.

If the user is not logged in, tell the user to run:

```bash
gws auth login
```

Beside, Service-account authentication is also supported when the user intentionally chooses it:

```bash
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
```

## Global Command Discovery

Start with help output instead of assuming exact command shapes:

```bash
gws --help
gws <service> --help
gws <service> <resource> --help
gws <service> <helper-or-resource> --help
```

Use schemas before calling raw API methods:

```bash
gws schema <service.resource.method>
gws schema <service.resource.method> --resolve-refs
```

Use `gws --help` to see the current list of supported services. Examples may include Gmail, Calendar, Drive, Sheets, Docs, Slides, Tasks, Keep, etc. 

## CLI Syntax

```bash
gws <service> <resource> [sub-resource] <method> [flags]
gws schema <service.resource.method> [--resolve-refs]
```

Examples:

```bash
gws drive files list --params '{"pageSize": 10}'
gws drive files get --params '{"fileId": "abc123"}'
gws sheets spreadsheets get --params '{"spreadsheetId": "..."}'
gws gmail users messages list --params '{"userId": "me"}'
gws schema drive.files.list
```

## Global Flags

<!-- markdownlint-disable MD013 -->

| Flag                    | Description                                              |
| ----------------------- | -------------------------------------------------------- |
| `--format <FORMAT>`     | Output format: `json` (default), `table`, `yaml`, `csv`  |
| `--dry-run`             | Validate locally without calling the API, when supported |
| `--sanitize <TEMPLATE>` | Screen responses through Model Armor                     |

## Method Flags

<!-- markdownlint-disable MD013 -->

| Flag                           | Description                                                       |
| ------------------------------ | ----------------------------------------------------------------- |
| `--params '{"key": "val"}'`    | URL/query parameters                                              |
| `--json '{"key": "val"}'`      | Request body                                                      |
| `-o, --output <PATH>`          | Save binary responses to file                                     |
| `--upload <PATH>`              | Upload file content as multipart media                            |
| `--upload-content-type <MIME>` | MIME type for uploaded content; otherwise inferred from extension |
| `--page-all`                   | Auto-paginate, one JSON page per line as NDJSON                   |
| `--page-limit <N>`             | Max pages when using `--page-all`                                 |
| `--page-delay <MS>`            | Delay between pages in milliseconds                               |

## Safety Rules

- Never output secrets, API keys, OAuth client secrets, tokens, encrypted credentials, or auth exports.
- Confirm with the user before executing any commands that is not read-only. Examples are writing emails, creating calendar events, uploading files, or deleting resources.
- Prefer `--dry-run` before destructive or externally visible operations when the command supports it.
- For read operations that may expose private emails, calendar details, files, contacts, or other PII, confirm with the user before proceeding.
- Use `--sanitize` when the user asks for Model Armor screening or when content safety/PII screening is required.

## Shell Tips

- JSON flags: wrap `--params` and `--json` values in single quotes so the shell does not interpret inner double quotes.

  ```bash
  gws drive files list --params '{"pageSize": 5}'
  ```

- zsh `!` expansion: Sheet ranges like `Sheet1!A1` contain `!`, which zsh may interpret as history expansion. Use double quotes with escaped inner quotes instead of single quotes.

  ```bash
  # WRONG in zsh
  gws sheets +read --spreadsheet ID --range 'Sheet1!A1:D10'

  # CORRECT
  gws sheets +read --spreadsheet ID --range "Sheet1!A1:D10"
  ```
