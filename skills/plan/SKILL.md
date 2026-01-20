---
name: plan
description: Agent Skill that brainstorm and produce a plan (not implementation). Use when the user asks for planning, a roadmap, an investigation/debug plan, or approach comparisons; gather context, ask clarifying questions, propose 1–3 options with tradeoffs, then produce a step-by-step plan with verification checkpoints and write it to a markdown file.
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

### Finalize + write to file

- Ask the user to save the final plan to a markdown file or not.
- If no, just output the plan in your response.
- If yes, save the finalized plan to a markdown file in the repo/workspace:
  - default path: `plans/` if it exists, else current directory
  - filename: `plan-<slug>-YYYYMMDD.md` (kebab-case slug)
- In your response: mention the file path and confirm you will follow the plan in subsequent steps.
