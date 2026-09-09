---
name: plan
description: Agent Skill for creating an implementation plan. Use when the user asks to plan, formalize, or save implementation work, or turn defined TODOs into sequenced, verifiable steps.
---

# Plan

Create an implementation plan that contains clear, self-contained, and verifiable steps. 

## Prerequisites

The user or you AI Agent should already have a clear context or clear direction in mind. If not, use `brainstorming` skill first

## Format of the plan

The plan should be written in markdown.

### Beginning format

The beginning format should be:

````markdown
# [Feature Name] Implementation Plan

## Goal
[No more than 3 sentences describing what this changes about]

## Context
[Any relevant context, background, scope, and success criteria]
[If there is a source-of-truth, such as the spec, issue, or a link, include it here]

## Approach
[2-3 sentences about the approach]
````

You can add more sections as needed.

## Steps Section

Begin with `## Steps` section like following:

````markdown
## Steps

When executing the plan:

- Mark `[ ]` boxes as completed `[x]` when item is completed
- After the imeplementation and verification of each step, spawn a subagent to do the code review, and fix any valuable feedbacks
  - If possible, reuse the same review subagent between steps
- Before moving to the next step, commit the changes
````

### Step format

For each step, placed inside the `## Steps` section with following structure:

````markdown
### [ ] Step N: [Step Name]

[One sentence describing what this step accomplishes]

[Optionally, a list of dependent steps in comma-separated one line list, beginnig with `**Depends on:**`]

#### Implementation

[Concise, concrete, and clear instructions for implementation]

#### Verification

[How to verify the implementation]

#### Notes

[Optional: any notes about this step, this section can be omitted if none]

````

## Reviewing the plan

After writing the plan, spawn a subagent with a fresh context window to review the plan. Address any valuable feedbacks from the subagent.
Run up to 3 review rounds, stopping early when a reviewer finds no actionable problems.

If the review agent spots a problem that needs more clarification or more planning work, or anything that invalidate the plan, surface the problem to the user for guidance.

## Writing the plan

By default, the plan should be saved in `plans/plan-<slug>-YYYYMMDD.md`.
However, project may have a different plans folder and/or different naming convention.
Always scan for project-specific plans folder and naming convention, and follow it if found.

## Notes

### About the overall procedure

- The plan file must be standalone and self-contained, which means, any one (including a new AI Agent) who is new to this project, can read the plan and start the implementation without guess work
- Make use of mermaid diagrams or ascii diagrams when they can clarify architecture, flow, state transition,compnents relationship, or any other explaination

### About each step

- When splitting the work into the step, split based on the size, and the high-cohesion low-coupling principle.
  - The size of each step should be a size reviewable by a human.
- Each step should be meaningful, self-contained, and self-verifiable.
- Include enough implementation detail to avoid guesswork, but do not turn the plan into a full code dump
  - Use snippets, interfaces, or pseudocode if they can help reduce ambiguity.
