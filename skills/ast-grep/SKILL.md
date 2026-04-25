---
name: ast-grep
description: Agent Skill for syntax-aware code search using `ast-grep`. Use when searching for code. Good at finding code patterns, structures, or relationships that are difficult to express with plain text search
compatibility: Requires the ast-grep CLI command `ast-grep`; `sg` may be available as a shorter alias.
---

# ast-grep Ad Hoc Search

Use `ast-grep` for syntax-aware, structural source-code search when text search
is too broad or fragile. This skill covers only one-off CLI searches with
`ast-grep run`, which is also the default subcommand.

## Scope

Use this skill for:

- Finding syntactic constructs such as calls, imports, decorators, assignments,
  conditionals, or function/class declarations.
- Searching with metavariables like `$FUNC($$$ARGS)` or `console.log($$$)`.
- Narrowing searches by language, path, globs, context lines, or JSON output.

Do not use this skill for:

- Creating persistent YAML rules, lint rules, project configs, or tests.
- Plain text search where `rg` is simpler and syntax does not matter.

## Default Workflow

1. Start with `ast-grep --help` or `ast-grep run --help` if option details may
   have changed.
2. Quote patterns with single quotes so the shell does not expand `$META`
   variables.
3. Prefer an explicit `--lang`/`-l` when searching a snippet, stdin, mixed
   extensions, or when inference may be ambiguous. Otherwise, ast-grep can infer
   language from file extensions.
4. Limit paths and globs early to keep results focused.
5. If results are surprising, inspect the parsed pattern with
   `--debug-query=ast` or add a `--selector` for the node kind to match.

## Command Basics

Use the full command name by default:

```sh
ast-grep run -p '<pattern>' -l <lang> <paths...>
```

The `run` subcommand is optional:

```sh
ast-grep -p '<pattern>' -l <lang> <paths...>
```

Useful options for ad hoc search:

- `-p, --pattern '<pattern>'`: AST pattern to match.
- `-l, --lang <lang>`: pattern language such as `ts`, `tsx`, `js`, `py`, `rs`,
  `go`, `java`, `yaml`, or `json`.
- `--globs '<glob>'`: include or exclude paths; repeat as needed and prefix
  exclusions with `!`.
- `-A`, `-B`, `-C`: show after, before, or surrounding context lines.
- `--json=stream`: output one JSON object per match for downstream processing.
- `--heading never`: print file paths inline, which is useful for piping.
- `--stdin`: search code provided on stdin.
- `--debug-query=ast`: show how the pattern parses; requires `--lang`.
- `--selector <kind>`: match a specific AST node from the parsed pattern.

## Pattern Rules of Thumb

- Patterns must be valid code, or close enough for the target tree-sitter parser
  to recover. If a fragment is ambiguous or incomplete, add surrounding context
  or use `--selector` to target the intended node.
- `$NAME` matches one named AST node. Metavariable names use uppercase letters,
  digits, and underscores.
- `$$$ARGS` matches zero or more AST nodes, commonly arguments, parameters, or
  statements.
- Reusing the same metavariable name requires the same syntax to appear in each
  position, such as `$A == $A`.
- Use names starting with underscore, such as `$_`, for throwaway non-capturing
  matches.
- Use `$$OP` only when you need to capture unnamed syntax nodes such as some
  operators; most ad hoc searches should start with normal `$META` variables.

## Examples

Find all JavaScript or TypeScript calls to `console.log` with any arguments:

```sh
ast-grep -p 'console.log($$$ARGS)' -l ts src
```

Find React hooks with any callback and dependency list in TSX files:

```sh
ast-grep -p 'useEffect($CALLBACK, $DEPS)' -l tsx --globs '**/*.tsx' src
```

Find Python functions with any parameters and body:

```sh
ast-grep -p 'def $FUNC($$$PARAMS): $$$BODY' -l py .
```

Find Rust `unwrap()` calls and show surrounding context:

```sh
ast-grep -p '$EXPR.unwrap()' -l rs -C 2 crates
```

Search stdin when the code comes from another command:

```sh
printf '%s\n' 'foo(bar)' | ast-grep --stdin -p '$FUNC($$$ARGS)' -l js
```

Produce machine-readable results:

```sh
ast-grep -p '$OBJ.$METHOD($$$ARGS)' -l ts --json=stream src
```

Debug a pattern that does not match as expected:

```sh
ast-grep -p 'console.log($$$)' -l js --debug-query=ast
```

## Search Strategy

- Prefer ast-grep over `rg` when the user describes code shape rather than exact
  text, for example "calls with any arguments", "same variable on both sides",
  "functions decorated with", or "imports from this module".
- Prefer `rg` first when searching comments, strings, documentation, arbitrary
  text, or exact identifiers without structural constraints.
- Combine both tools when useful: use `rg` to discover candidate files or terms,
  then ast-grep to verify syntax-aware matches.
- Keep patterns simple. If a one-liner pattern needs complex relational logic,
  tell the user that persistent ast-grep rules are outside this skill's scope
  and ask whether they want to switch to rule authoring.
