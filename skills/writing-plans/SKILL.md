---
name: writing-plans
description: Agent Skill for writing comprehensive implementation plans with bite-sized tasks. Use when you have a spec, requirements, or approved design for a multi-step task, before touching code. Can also be invoked standalone to gather context and plan from scratch.
metadata:
  attribution: attribution.md
---

# Writing Plans

## Overview

Write comprehensive implementation plans assuming the implementer has very
little context for the codebase or problem domain. Document the files, code,
tests, docs, commands, and verification they need. Keep plans bite-sized, DRY,
YAGNI, and TDD-oriented when applicable.

Default save path: `plans/plan-<slug>-YYYYMMDD.md`

User preferences for the plan location override this default.

## Standalone Use

If this skill is invoked without a prior spec or design:

1. Gather context from the codebase, docs, configs, and any related issues
2. Clarify goals, constraints, and success criteria with the user
3. Propose 1-3 approaches or scope options when there is a real trade-off
4. Once direction is confirmed, write the detailed implementation plan

When todo tools or skills are available, use them to track planning progress.

## Scope Check

If the spec or requirements cover multiple independent subsystems, suggest
breaking the work into separate plans, one per subsystem. Each plan should
produce working, testable software on its own.

## File Structure

Before defining tasks, map out which files will be created or modified and what
each one is responsible for. This is where decomposition decisions get locked
in.

- Design units with clear boundaries and well-defined interfaces. Each file
  should have one clear responsibility.
- Prefer smaller, focused files over large ones that do too much.
- Files that change together should live together. Split by responsibility, not
  by technical layer.
- In existing codebases, follow established patterns. If a file you are
  modifying has grown unwieldy, including a split in the plan is reasonable.

This structure informs the task decomposition. Each task should produce
self-contained changes that make sense independently.

## Bite-Sized Task Granularity

Each step is one action that usually takes 2-5 minutes:

- "Write the failing test"
- "Run it to make sure it fails"
- "Implement the minimal code to make the test pass"
- "Run the tests and make sure they pass"
- "Commit"

If TDD is not applicable, for example config-only or documentation-only
changes, replace the failing-test steps with the smallest meaningful
verification steps.

## Plan Document Header

Every plan MUST start with this header:

````markdown
# [Feature Name] Implementation Plan

> **For agentic workers:** Use the harness's preferred task-tracking and
> delegation tools when available. Steps use checkbox (`- [ ]`) syntax for
> tracking.

**Goal:** [One sentence describing what this builds]

**Architecture:** [2-3 sentences about approach]

**Tech Stack:** [Key technologies or libraries]

---
````

## Task Structure

````markdown
### Task N: [Component Name]

**Files:**
- Create: `exact/path/to/file.py`
- Modify: `exact/path/to/existing.py:123-145`
- Test: `tests/exact/path/to/test.py`

- [ ] **Step 1: Write the failing test**

```python
def test_specific_behavior():
  result = function(input)
  assert result == expected
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/path/test.py::test_name -v`
Expected: FAIL with "function not defined"

- [ ] **Step 3: Write minimal implementation**

```python
def function(input):
  return expected
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/path/test.py::test_name -v`
Expected: PASS

- [ ] **Step 5: Commit**

```bash
git add tests/path/test.py src/path/file.py
git commit -m "feat: add specific feature"
```
````

## Remember

- Exact file paths always
- Complete code in the plan, not vague instructions like "add validation"
- Exact commands with expected output
- Use Mermaid diagrams and ASCII diagrams when a plan needs a visual
- Reference relevant skills when they materially help execution
- DRY, YAGNI, TDD, and frequent commits

## Plan Review Loop

After completing each chunk of the plan:

1. Dispatch a plan-document-reviewer subagent using
   `references/plan-document-reviewer-prompt.md` with precisely crafted review
   context, never your session history
2. If issues are found, fix the chunk, re-dispatch the reviewer, and repeat
   until approved
3. If approved, proceed to the next chunk or the execution handoff if it is the
   last chunk

Use `## Chunk N: <name>` headings to delimit chunks. Each chunk should be under
1000 lines and logically self-contained.

If the review loop exceeds 5 iterations, surface the problem to a human for
guidance.

## Execution Handoff

After saving the plan:

> "Plan complete and saved to `<path>`. Review it and let me know how you'd
> like to execute it."

Present the plan to the user and ask for instructions for execution.
