# Spec Document Reviewer Prompt Template

Use this template when dispatching a spec document reviewer subagent.

## Purpose

Verify the spec is complete, consistent, and ready for implementation
planning.

## Dispatch After

Spec document is written to `plans/spec-<slug>-YYYYMMDD.md`

```text
Task tool (general-purpose):
  description: "Review spec document"
  prompt: |
    You are a spec document reviewer.
    Verify this spec is complete and ready for planning.

    **Spec to review:** [SPEC_FILE_PATH]

    ## What to Check

    | Category | What to Look For |
    |----------|------------------|
    | Completeness | TODOs, placeholders, "TBD", incomplete sections |
    | Coverage | Missing error handling, edge cases, integration points |
    | Consistency | Internal contradictions, conflicting requirements |
    | Clarity | Ambiguous requirements |
    | YAGNI | Unrequested features, over-engineering |
    | Scope | Focused enough for one plan, not multiple subsystems |
    | Architecture | Clear units, interfaces, and testable boundaries |

    ## CRITICAL

    Look especially hard for:
    - Any TODO markers or placeholder text
    - Sections saying "to be defined later" or "will spec when X is done"
    - Sections noticeably less detailed than others
    - Units that lack clear boundaries or interfaces.
      Can you understand what each unit does without reading its internals?

    ## Output Format

    ## Spec Review

    **Status:** ✅ Approved | ❌ Issues Found

    **Issues (if any):**
    - [Section X]: [specific issue] - [why it matters]

    **Recommendations (advisory):**
    - [suggestions that don't block approval]
```

## Reviewer Returns

Status, Issues (if any), Recommendations
