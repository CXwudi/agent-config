---
name: plan
description: Agent Skill for brainstorming and producing a plan (not implementation). Use when the user asks for planning, roadmaps, investigation/debug plans, or approach comparisons. Output step-by-step verification checkpoints.
---

# Plan

Brainstorm and produce an actionable plan.

## Rules

- Default to planning only: do **not** edit project source/business code unless the user explicitly asks you to implement.
- Allowed: throw-away scripts/snippets/commands for analysis, verification, or proof-of-concept.

## Workflow

### Gather context

- Read relevant local docs/source/config.
- If needed for accuracy (e.g., “latest/current”), ask permission to browse the web, then gather sources.

### Clarify

- Ask open questions until goals, constraints, and success criteria are clear.
- Confirm what “done” looks like and any constraints (time, budget, tech stack, permissions, deadline).

### Propose 1 to 3 options

- If only one option, just confirm with the user before proceeding.
- Otherwise, for each option: summary, key steps, pros/cons, risks, and how to verify.
  - Explain tradeoffs between options.
  - Recommend one option, explain why, and ask for user confirmation to choose one option.

### Produce the step-by-step plan

- Once the user picks an option (or confirms the recommendation), to come up with a detailed step-by-step plan, you need to proactively ask users about the details of each step. Do not assume anything.
  - For each step, you ask question to clarify the details of the step.
  - If still unclear, explicit “open questions / assumptions” section
- In detailed step-by-step plan, a verification step/checkpoint should be added after each major step, to ensure correctness (tests/build/lint/typecheck/etc.).

REMEMBER: The goal is to eliminate as much ambiguity as possible as early as possible.

### Finalize + Record the plan

- Ask the user to save the final plan to a markdown file or not.
- If no, just output the plan in your response.
- If yes, save the finalized plan to a markdown file in the repo/workspace:
  - default path: `plans/` if it exists, else current directory
  - filename: `plan-<slug>-YYYYMMDD.md` (kebab-case slug)
  - Also use the `context-skill` Agent SKill to record any related context at the end of the markdown file.
  - In your response: mention the file path
- When the user ask you to start the plan, if you have Todo tools/skills, create a todo list for the plan steps to help you track and manage the progress.
