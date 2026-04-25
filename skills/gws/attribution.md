# Attribution

This skill was adapted from `googleworkspace/cli`.

## Upstream Source

- Repository: `https://github.com/googleworkspace/cli`
- Version: `v0.22.5`
- License: `Apache License 2.0`
- License file: `https://github.com/googleworkspace/cli/blob/v0.22.5/LICENSE`

## Source Files

- Source root:
  `https://github.com/googleworkspace/cli/tree/v0.22.5/skills/gws-shared`
- Files:
  - `SKILL.md`

## Local Files Covered

- `SKILL.md`

## Local Adaptation Notes

- Renamed the local skill to `gws` so it can cover all `gws`-supported Google
  Workspace services through command discovery rather than generated per-service
  skills.
- Kept the upstream shared CLI syntax, global flags, method flags, security
  rules, shell tips, and feedback etiquette.
- Added local authentication workflow guidance: check `gws auth status` first,
  run interactive `gws auth login` when needed, and ask for
  `~/.config/gws/client_secret.json` if OAuth client credentials are missing.
- Added explicit instructions to use `gws --help`, service help, resource help,
  and `gws schema` instead of embedding generated command references.
