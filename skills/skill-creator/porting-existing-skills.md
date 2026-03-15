# Porting Existing Skills

Read this file when a skill is adapted from an external upstream source.

## Required Steps

1. Create a per-skill `attribution.md` using
   [references/template/attribution.md](references/template/attribution.md).
2. Update `skills/THIRD_PARTY_NOTICES.md`. This file is the single source of
   truth for third-party provenance, version pinning, attribution index,
   license details, and full third-party license text.
3. Add or update the ported skill entry in the notice-file summary table.
4. Add `metadata.attribution: attribution.md` to the ported skill's
   `SKILL.md` frontmatter.
5. Keep `skills/README.md` minimal and point readers to
   `THIRD_PARTY_NOTICES.md`.
6. Use canonical GitHub URLs pinned to a tag or commit.
7. Never use local cache paths such as `~/.claude/...`.
8. Include exact upstream license text in `THIRD_PARTY_NOTICES.md` when the
   license requires inclusion.
9. Document local adaptation notes factually.
10. If a ported skill also incorporates pre-existing local behavior, record
    that as a local adaptation note, not as a third-party dependency.
