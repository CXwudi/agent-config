# Attribution

This skill was adapted from `obra/superpowers`.

## Upstream Source

- Repository: `https://github.com/obra/superpowers`
- Version: `v5.0.2`
- License: `MIT License`
- License file:
  `https://github.com/obra/superpowers/blob/v5.0.2/LICENSE`

## Source Files

- Source root:
  `https://github.com/obra/superpowers/tree/v5.0.2/skills/writing-plans`
- Files:
  - `SKILL.md`
  - `plan-document-reviewer-prompt.md`

## Local Files Covered

- `SKILL.md`
- `references/plan-reviewer-prompt.md`

## Local Adaptation Notes

- Substantially rewritten into a plan-centric skill focused on shaping
  execution strategy rather than writing a document artifact.
- Renamed the local skill identity and on-disk directory to `plan`.
- Switched plan save paths to `plans/plan-<slug>-YYYYMMDD.md`.
- Replaced superpowers-specific execution guidance with generic wording.
- Reworked planning guidance around source of truth, adaptive planning depth,
  execution reliability, and explicit verification.
- Made `reference-recorder` a required dependency for generating the
  `## References` section in every saved plan.
- Replaced chunk-based multi-subagent review guidance with adaptive self-review
  plus optional whole-plan reviewer subagent flow.
- Replaced the local chunk-oriented reviewer prompt with
  `references/plan-reviewer-prompt.md` for whole-plan review.
