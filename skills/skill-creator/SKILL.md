---
name: skill-creator
description: Agent Skill for creating new skills according to the official specification. Use when asked to create or update a skill, and follow the specification at https://agentskills.io/specification.md.
---

# Skill Creator

The procedure is very straightforward, use `curl` or web crawl tool to fetch the latest skill specification at [offcial documentation site](https://agentskills.io/specification.md) and strictly follow the specification to create the new skill.

If no web access, a copy is available at [references/specification.md](references/specification.md), but it may be outdated. So prefer web access if possible.

## User Convienience

Description field format: 3 sentences:

1. A short intro of the skill, usually within 10 words (E.g. "Agent Skill of ...", "Skill for ...", etc.)
2. A sentence about when to use this skill (E.g. "Use when ...", "Ideal to ...", "Prefer this skill for ...", etc.)
3. (Optional) Anything else helps agent decide when to use this skill
