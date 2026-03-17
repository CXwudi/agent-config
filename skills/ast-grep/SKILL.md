---
name: ast-grep
description: Agent Skill for writing ast-grep rules for structural code search and analysis. Use when users need to search codebases with Abstract Syntax Tree (AST) patterns, find specific language constructs, or run code queries that go beyond simple text matching. Prefer this skill for structural code lookups in ast-grep-supported languages, especially when plain text search would be too imprecise.
license: MIT
compatibility: Requires the ast-grep CLI to be installed and available in PATH.
metadata:
  attribution: attribution.md
---

# ast-grep Code Search

## Overview

This skill helps translate natural language queries into ast-grep rules for
structural code search. ast-grep uses Abstract Syntax Tree (AST) patterns to
match code based on its structure rather than just text, enabling powerful and
precise code search across large codebases.

## When to Use This Skill

Use this skill when users:

- Need to search for code patterns using structural matching, such as finding
  async functions that do not have error handling
- Want to locate specific language constructs, such as function calls with
  specific parameters
- Request searches that require understanding code structure rather than just
  text
- Ask to search for code with particular AST characteristics
- Need to perform complex code queries that traditional text search cannot
  handle

## General Workflow

Follow this process to help users write effective ast-grep rules:

### Step 1: Understand the Query

Clearly understand what the user wants to find. Ask clarifying questions if
needed:

- What specific code pattern or structure are they looking for?
- Which programming language?
- Are there specific edge cases or variations to consider?
- What should be included or excluded from matches?

### Step 2: Create Example Code

Write a simple code snippet that represents what the user wants to match. Save
this to a temporary file for testing.

Example:

```javascript
// test_example.js
async function example() {
  const result = await fetchData();
  return result;
}
```

### Step 3: Write the ast-grep Rule

Translate the pattern into an ast-grep rule. Start simple and add complexity as
needed.

Key principles:

- Always use `stopBy: end` for relational rules like `inside` and `has` to
  ensure search goes to the end of the direction
- Use `pattern` for simple structures
- Use `kind` with `has` or `inside` for complex structures
- Break complex queries into smaller sub-rules using `all`, `any`, or `not`

Example rule file, `test_rule.yml`:

```yaml
id: async-with-await
language: javascript
rule:
  kind: function_declaration
  has:
    pattern: await $EXPR
    stopBy: end
```

See `references/rule_reference.md` for comprehensive rule documentation.

### Step 4: Test the Rule

Use ast-grep CLI to verify the rule matches the example code. There are two
main approaches:

Option A, test with inline rules for quick iterations:

```bash
echo "async function test() { await fetch(); }" \
  | ast-grep scan --inline-rules "id: test
language: javascript
rule:
  kind: function_declaration
  has:
    pattern: await \$EXPR
    stopBy: end" --stdin
```

Option B, test with rule files for more complex rules:

```bash
ast-grep scan --rule test_rule.yml test_example.js
```

Debugging if there are no matches:

1. Simplify the rule by removing sub-rules
2. Add `stopBy: end` to relational rules if it is not present
3. Use `--debug-query` to understand the AST structure
4. Check if `kind` values are correct for the language

### Step 5: Search the Codebase

Once the rule matches the example code correctly, search the actual codebase.

For simple pattern searches:

```bash
ast-grep run --pattern 'console.log($ARG)' --lang javascript /path/to/project
```

For complex rule-based searches:

```bash
ast-grep scan --rule my_rule.yml /path/to/project
```

For inline rules without creating files:

```bash
ast-grep scan --inline-rules "id: my-rule
language: javascript
rule:
  pattern: \$PATTERN" /path/to/project
```

## ast-grep CLI Commands

### Inspect Code Structure with `--debug-query`

Dump the AST structure to understand how code is parsed:

```bash
ast-grep run --pattern 'async function example() { await fetch(); }' \
  --lang javascript \
  --debug-query=cst
```

Available formats:

- `cst`: Concrete Syntax Tree, which shows all nodes including punctuation
- `ast`: Abstract Syntax Tree, which shows only named nodes
- `pattern`: Shows how ast-grep interprets your pattern

Use this to:

- Find the correct `kind` values for nodes
- Understand the structure of code you want to match
- Debug why patterns are not matching

Example:

```bash
# See the structure of your target code
ast-grep run --pattern 'class User { constructor() {} }' \
  --lang javascript \
  --debug-query=cst

# See how ast-grep interprets your pattern
ast-grep run --pattern 'class $NAME { $$$BODY }' \
  --lang javascript \
  --debug-query=pattern
```

### Test Rules with `scan --stdin`

Test a rule against a code snippet without creating files:

```bash
echo "const x = await fetch();" | ast-grep scan --inline-rules "id: test
language: javascript
rule:
  pattern: await \$EXPR" --stdin
```

Add `--json` for structured output:

```bash
echo "const x = await fetch();" | ast-grep scan --inline-rules "..." --stdin --json
```

### Search with Patterns using `run`

Simple pattern-based search for single AST node matches:

```bash
# Basic pattern search
ast-grep run --pattern 'console.log($ARG)' --lang javascript .

# Search specific files
ast-grep run --pattern 'class $NAME' --lang python /path/to/project

# JSON output for programmatic use
ast-grep run --pattern 'function $NAME($$$)' --lang javascript --json .
```

When to use:

- Simple, single-node matches
- Quick searches without complex logic
- Cases where you do not need relational rules like `inside` or `has`

### Search with Rules using `scan`

YAML rule-based search for complex structural queries:

```bash
# With rule file
ast-grep scan --rule my_rule.yml /path/to/project

# With inline rules
ast-grep scan --inline-rules "id: find-async
language: javascript
rule:
  kind: function_declaration
  has:
    pattern: await \$EXPR
    stopBy: end" /path/to/project

# JSON output
ast-grep scan --rule my_rule.yml --json /path/to/project
```

When to use:

- Complex structural searches
- Relational rules like `inside`, `has`, `precedes`, and `follows`
- Composite logic like `all`, `any`, and `not`
- Cases where you need the power of full YAML rules

Tip: For relational rules like `inside` and `has`, always add `stopBy: end` to
ensure complete traversal.

## Tips for Writing Effective Rules

### Always Use `stopBy: end`

For relational rules, always use `stopBy: end` unless there is a specific
reason not to:

```yaml
has:
  pattern: await $EXPR
  stopBy: end
```

This ensures the search traverses the entire subtree rather than stopping at
the first non-matching node.

### Start Simple, Then Add Complexity

Begin with the simplest rule that could work:

1. Try a `pattern` first
2. If that does not work, try `kind` to match the node type
3. Add relational rules like `has` and `inside` as needed
4. Combine with composite rules like `all`, `any`, and `not` for complex logic

### Use the Right Rule Type

- Pattern: For simple, direct code matching such as `console.log($ARG)`
- Kind plus relational rules: For complex structures such as a function
  containing `await`
- Composite rules: For logical combinations such as a function with `await`
  but not in `try-catch`

### Debug with AST Inspection

When rules do not match:

1. Use `--debug-query=cst` to see the actual AST structure
2. Check if metavariables are being detected correctly
3. Verify the node `kind` matches what you expect
4. Ensure relational rules are searching in the right direction

### Escaping in Inline Rules

When using `--inline-rules`, escape metavariables in shell commands:

- Use `\$VAR` instead of `$VAR`, because the shell interprets `$` as a variable
- Or use single quotes, since `'$VAR'` works in most shells

Example:

```bash
# Correct: escaped $
ast-grep scan --inline-rules "rule: {pattern: 'console.log(\$ARG)'}" .

# Or use single quotes
ast-grep scan --inline-rules 'rule: {pattern: "console.log($ARG)"}' .
```

## Common Use Cases

### Find Functions with Specific Content

Find async functions that use `await`:

```bash
ast-grep scan --inline-rules "id: async-await
language: javascript
rule:
  all:
    - kind: function_declaration
    - has:
        pattern: await \$EXPR
        stopBy: end" /path/to/project
```

### Find Code Inside Specific Contexts

Find `console.log` inside class methods:

```bash
ast-grep scan --inline-rules "id: console-in-class
language: javascript
rule:
  pattern: console.log(\$\$\$)
  inside:
    kind: method_definition
    stopBy: end" /path/to/project
```

### Find Code Missing Expected Patterns

Find async functions without `try-catch`:

```bash
ast-grep scan --inline-rules "id: async-no-trycatch
language: javascript
rule:
  all:
    - kind: function_declaration
    - has:
        pattern: await \$EXPR
        stopBy: end
    - not:
        has:
          pattern: try { \$\$\$ } catch (\$E) { \$\$\$ }
          stopBy: end" /path/to/project
```

## Resources

The `references/` directory contains detailed documentation for ast-grep rule
syntax:

- `rule_reference.md`: Comprehensive ast-grep rule documentation covering
  atomic rules, relational rules, composite rules, and metavariables

Load these references when detailed rule syntax information is needed.
