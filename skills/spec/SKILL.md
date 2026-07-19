---
name: spec
description: Agent Skill for writing a design spec. Use when the user asks to write, formalize, or save a spec, design document, RFC, or a proposal.
---

# Spec

Turn a settled design direction into a well defined spec artifact

## Prerequisites

User or you already have a clear context or design in mind. If not, use `brainstorming` skill first

## Format of the spec

The spec should be written in markdown following the following structure:

````markdown
# [Feature Name] Design Spec

## Design Goal
[What problem this solves and why it matters]

## Context
[Any relevant context, background, and constraints]

## Design Decision
[Chosen direction, full detail description of the locked design, why it was selected, and the key implications]
[If needed, this section can be broken down into several h3 sections for clarity]

### Alternatives Considered
[One h4 section per alternative]
[Briefly note rejected alternatives, why it is rejected] 

## Scopes

### In Scope

[What this spec covers, in bullet points]

### Out of Scope

[What is intentionally excluded, in bullet points]

## Risks and Open Questions

[Any risk, assumption, unresolved questions, open-end questions, or any other concerns]
[Can either be a bullet list, or one h3 section per risk/question]

## Validation Considerations
[How the design should be validated once implemented]

## References
[Generated via `reference-recorder`]
````

## Reviewing the spec

After writing the spec, spawn a subagent with fresh context window to review the spec.
Address any valuable feedback, then repeat this review process again (only 2 times in total).

If the review agent spots a problem that needs more brainstorming, more context, more clarification or more design work, or anything that invalidate the spec, surface the problem to the user for guidance.

## Writing the spec

By default, the spec should be saved in `specs/spec-<slug>-YYYYMMDD.md`.
However, project may have a different specs folder and/or different naming convention.
Always scan for project-specific spec folder and naming convention, and follow it if found.

## Notes

- the spec file must be standalone and self-contained, which means, any one (including a new AI Agent) who is new to this project, can read the spec and understand it
- Make sure of mermaid diagrams or ascii diagrams when they can clarify architecture, flow, state transition,compnents relationship, or any other design aspect
