---
name: skill-creator
description: Agent Skill for creating new skills according to the official specification. Use when asked to create or update a skill, and follow specifications from https://agentskills.io/.
---

# Skill Creator

The procedure is very straightforward.
Use `curl` or web crawl tool to fetch and follow guides from various pages in
[official documentation site](https://agentskills.io/).
Strictly follow the following:

## Specification

First, follow the official specification at
[specification](https://agentskills.io/skill-creation/specification.md).

## Optimizing Descriptions

For improving description triggering accuracy, follow the guide at
[optimizing descriptions](https://agentskills.io/skill-creation/optimizing-descriptions.md),
while ensure the following user conventions are followed:

### User Conventions

Description field format: 3 parts:

1. A short intro of the skill, usually within 10 words.
   E.g. "Agent Skill of ...", "Skill for ...", etc.
2. A sentence about when to use this skill.
   E.g. "Use when ...", "Ideal to ...", "Prefer this skill for ...", etc.
3. Optional: anything else helps the agent decide when to use this skill, or
   when not to use it. Can be one or more sentences.

## Evaluation

After creating or updating a skill, evaluate its output quality. Follow the
eval framework at
[evaluating skills](https://agentskills.io/skill-creation/evaluating-skills.md).

## Using Scripts

For bundling scripts in skills, follow the guide at
[using scripts](https://agentskills.io/skill-creation/using-scripts.md).

## Porting Existing Skills

If you are adapting a skill from an external upstream source,
also follow the instruction in
[porting-existing-skills](porting-existing-skills.md).

## Offline Fallback

If no web access, local copies are available but may be outdated.
Prefer web access if possible.

- Specification:
  [references/agent-skills-spec/specification.md](references/agent-skills-spec/specification.md)
- Optimizing Descriptions:
  [references/agent-skills-spec/optimizing-descriptions.md](references/agent-skills-spec/optimizing-descriptions.md)
- Evaluating Skills:
  [references/agent-skills-spec/evaluating-skills.md](references/agent-skills-spec/evaluating-skills.md)
- Using Scripts:
  [references/agent-skills-spec/using-scripts.md](references/agent-skills-spec/using-scripts.md)
- Attribution Template:
  [references/template/attribution.md](references/template/attribution.md)
