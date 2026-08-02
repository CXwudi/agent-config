---
name: ast-grep
description: Agent Skill for syntax-aware code search using `ast-grep`. Use when searching for code. Good at finding code patterns, structures, or relationships that are difficult to express with plain text search
compatibility: Requires the ast-grep CLI command `ast-grep`; `sg` may be available as a shorter alias.
---

# ast-grep Ad Hoc Search

Use `ast-grep` for syntax-aware, structural source-code search when text search is too broad or fragile. This skill covers only one-off CLI searches with `ast-grep run`.

## Command Basics

Run:

```
ast-grep run --help
```

To understand how to use `ast-grep run` for ad hoc searches.

Useful options for ad hoc search:

- `-p, --pattern '<pattern>'`: AST pattern to match.
- `-l, --lang <lang>`: pattern language such as `ts`, `tsx`, `js`, `py`, `rs`, `go`, `java`, `yaml`, or `json`.
- `--globs '<glob>'`: include or exclude paths; repeat as needed and prefix exclusions with `!`.
- `-A`, `-B`, `-C`: show after, before, or surrounding context lines.
- `--json=stream`: output one JSON object per match for downstream processing.
- `--heading never`: print file paths inline, which is useful for piping.
- `--stdin`: search code provided on stdin.
- `--debug-query=ast`: show how the pattern parses; requires `--lang`.
- `--selector <kind>`: match a specific AST node from the parsed pattern.

## Pattern Rules of Thumb

- Patterns must be valid code, or close enough for the target tree-sitter parser to recover. If a fragment is ambiguous or incomplete, add surrounding context or use `--selector` to target the intended node.
- Quote patterns with single quotes so the shell does not expand `$META` variables.
- `$NAME` matches one named AST node. Metavariable names use uppercase letters, digits, and underscores.
- `$$$ARGS` matches zero or more AST nodes, commonly arguments, parameters, or statements.
- Reusing the same metavariable name requires the same syntax to appear in each position, such as `$A == $A`.
- Use names starting with underscore, such as `$_`, for throwaway non-capturing matches.
- Use `$$OP` only when you need to capture unnamed syntax nodes such as some operators; most ad hoc searches should start with normal `$META` variables.

## Search Strategy

- Prefer ast-grep over `rg` when the user describes code shape rather than exact text, for example "calls with any arguments", "same variable on both sides", "functions decorated with", or "imports from this module".
- Prefer `rg` first when searching comments, strings, documentation, arbitrary text, or exact identifiers without structural constraints.
- Combine both tools when useful: use `rg` to discover candidate files or terms, then ast-grep to verify syntax-aware matches.
- Keep patterns simple. If a one-liner pattern needs complex relational logic, tell the user that persistent ast-grep rules are outside this skill's scope and ask whether they want to switch to rule authoring.
