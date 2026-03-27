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
  `https://github.com/obra/superpowers/tree/v5.0.2/skills/brainstorming`
- Files:
  - `SKILL.md`
  - `spec-document-reviewer-prompt.md`

## Local Files Covered

- `SKILL.md`
- `references/spec-document-reviewer-prompt.md`

## Local Adaptation Notes

- Narrowed the skill trigger to underdefined or tradeoff-heavy work instead of
  treating every project as mandatory brainstorming.
- Switched design save paths to `spec/spec-<slug>-YYYYMMDD.md`.
- Reworked the workflow around recommending one design, mentioning viable
  alternatives, and explaining why they were not chosen.
- Made `reference-recorder` a required dependency for generating the
  `## References` section in every saved spec.
- Made spec review mandatory and required user review of the saved spec before
  handing off to `plan`.
- Removed the commit requirement for saved specs unless explicitly requested.
- Replaced Graphviz diagrams with Mermaid and allowed ASCII fallback.
- Made review and implementation handoff wording agent-agnostic.
