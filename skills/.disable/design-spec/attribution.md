# Attribution

This skill was split from the local `brainstorming` skill, which was adapted from `obra/superpowers`.

## Upstream Source

- Repository: `https://github.com/obra/superpowers`
- Version: `v5.0.2`
- License: `MIT License`
- License file: `https://github.com/obra/superpowers/blob/v5.0.2/LICENSE`

## Source Files

- Source root: `https://github.com/obra/superpowers/tree/v5.0.2/skills/brainstorming`
- Files:
  - `SKILL.md`
  - `spec-document-reviewer-prompt.md`

## Local Files Covered

- `SKILL.md`
- `references/spec-document-reviewer-prompt.md`

## Local Adaptation Notes

- Split the durable spec workflow out of `brainstorming`.
- Kept mandatory spec writing, reference generation, spec review, user review, and handoff to `plan`.
- Clarified that `design-spec` captures settled decisions and redirects open trade-offs back to `brainstorming`.
- Preserved the `spec/spec-<slug>-YYYYMMDD.md` save path and mandatory `reference-recorder` dependency.
