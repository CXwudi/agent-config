# ast-grep Rule Reference

This document provides comprehensive documentation for ast-grep rule syntax,
covering all rule types and metavariables.

## Introduction to ast-grep Rules

ast-grep rules are declarative specifications for matching and filtering
Abstract Syntax Tree (AST) nodes. They enable structural code search and
analysis by defining conditions an AST node must meet to be matched.

### Rule Categories

ast-grep rules are categorized into three types:

- Atomic Rules: Match individual AST nodes based on intrinsic properties like
  code patterns (`pattern`), node type (`kind`), or text content (`regex`).
- Relational Rules: Define conditions based on a target node's position or
  relationship to other nodes, such as `inside`, `has`, `precedes`, and
  `follows`.
- Composite Rules: Combine other rules using logical operations like `all`,
  `any`, `not`, and `matches` to form complex matching criteria.

## Anatomy of an ast-grep Rule Object

The ast-grep rule object is the core configuration unit defining how ast-grep
identifies and filters AST nodes. It is typically written in YAML format.

### General Structure

Every field within an ast-grep Rule Object is optional, but at least one
positive key such as `kind` or `pattern` must be present.

A node matches a rule if it satisfies all fields defined within that rule
object, implying an implicit logical `AND` operation.

For rules using metavariables that depend on prior matching, explicit `all`
composite rules are recommended to guarantee execution order.

### Rule Object Properties

Key properties:

- `pattern`
  Type: String or Object. Category: Atomic.
  Matches an AST node by code pattern. Example:
  `pattern: console.log($ARG)`.
- `kind`
  Type: String. Category: Atomic.
  Matches an AST node by its kind name. Example:
  `kind: call_expression`.
- `regex`
  Type: String. Category: Atomic.
  Matches node text by Rust regex. Example: `regex: ^[a-z]+$`.
- `nthChild`
  Type: number, string, or Object. Category: Atomic.
  Matches nodes by index within a parent's children. Example:
  `nthChild: 1`.
- `range`
  Type: RangeObject. Category: Atomic.
  Matches a node by character-based start and end positions. Example:
  `range: { start: { line: 0, column: 0 }, end: { line: 0, column: 10 } }`.
- `inside`
  Type: Object. Category: Relational.
  The target node must be inside a node matching the sub-rule. Example:
  `inside: { pattern: class $C { $$$ }, stopBy: end }`.
- `has`
  Type: Object. Category: Relational.
  The target node must have a descendant matching the sub-rule. Example:
  `has: { pattern: await $EXPR, stopBy: end }`.
- `precedes`
  Type: Object. Category: Relational.
  The target node must appear before a node matching the sub-rule. Example:
  `precedes: { pattern: return $VAL }`.
- `follows`
  Type: Object. Category: Relational.
  The target node must appear after a node matching the sub-rule. Example:
  `follows: { pattern: import $M from '$P' }`.
- `all`
  Type: array of rules. Category: Composite.
  Matches if all sub-rules match. Example:
  `all: [{ kind: call_expression }, { pattern: foo($A) }]`.
- `any`
  Type: array of rules. Category: Composite.
  Matches if any sub-rules match. Example:
  `any: [{ pattern: foo() }, { pattern: bar() }]`.
- `not`
  Type: Object. Category: Composite.
  Matches if the sub-rule does not match. Example:
  `not: { pattern: console.log($ARG) }`.
- `matches`
  Type: String. Category: Composite.
  Matches if a predefined utility rule matches. Example:
  `matches: my-utility-rule-id`.

## Atomic Rules

Atomic rules match individual AST nodes based on their intrinsic properties.

### `pattern`: String and Object Forms

The `pattern` rule matches a single AST node based on a code pattern.

String pattern:

```yaml
pattern: console.log($ARG)
```

Object pattern:

```yaml
pattern:
  selector: field_definition
  context: class { $F }
```

This form offers granular control for ambiguous patterns or specific contexts.
`context` provides surrounding code for correct parsing. `strictness` modifies
the pattern's matching algorithm, such as `cst`, `smart`, `ast`, `relaxed`, or
`signature`.

### `kind`: Matching by Node Type

The `kind` rule matches an AST node by its `tree_sitter_node_kind` name,
derived from the language's Tree-sitter grammar. This is useful for targeting
constructs like `call_expression` or `function_declaration`.

```yaml
kind: call_expression
```

### `regex`: Text-Based Node Matching

The `regex` rule matches the entire text content of an AST node using a Rust
regular expression. It is not a positive rule, which means it can match any
node whose text satisfies the regex regardless of its structural kind.

### `nthChild`: Positional Node Matching

The `nthChild` rule finds nodes by their 1-based index within their parent's
children list, counting only named nodes by default.

- `number`: Matches the exact nth child, such as `nthChild: 1`
- `string`: Matches positions using the An+B formula, such as `2n+1`
- `Object`: Provides granular control
  - `position`: a `number` or An+B string
  - `reverse`: `true` to count from the end
  - `ofRule`: an ast-grep rule used to filter the sibling list before counting

### `range`: Position-Based Node Matching

The `range` rule matches an AST node based on its character-based start and end
positions. A `RangeObject` defines `start` and `end` fields, each with 0-based
`line` and `column`. `start` is inclusive and `end` is exclusive.

## Relational Rules

Relational rules filter targets based on their position relative to other AST
nodes. They can include `stopBy` and `field` options.

### `inside`: Matching Within a Parent Node

This requires the target node to be inside another node matching the `inside`
sub-rule.

```yaml
inside:
  pattern: class $C { $$$ }
  stopBy: end
```

### `has`: Matching with a Descendant Node

This requires the target node to have a descendant node matching the `has`
sub-rule.

```yaml
has:
  pattern: await $EXPR
  stopBy: end
```

### `precedes` and `follows`: Sequential Node Matching

- `precedes`: The target node must appear before a node matching the
  `precedes` sub-rule
- `follows`: The target node must appear after a node matching the `follows`
  sub-rule

Both support `stopBy`, but not `field`.

### `stopBy` and `field`: Refining Relational Searches

`stopBy` controls search termination for relational rules.

- `neighbor`, the default, stops when the immediate surrounding node does not
  match
- `end` searches to the end of the direction, which means the root for
  `inside` and the leaf for `has`
- A rule object stops when a surrounding node matches the provided rule, and it
  is inclusive

`field` specifies a sub-node within the target node that should match the
relational rule. It only applies to `inside` and `has`.

Best practice: When unsure, always use `stopBy: end` to ensure the search goes
to the end of the direction.

## Composite Rules

Composite rules combine atomic and relational rules using logical operations.

### `all`: Conjunction of Rules

This matches a node only if all sub-rules in the list match. It also guarantees
rule-matching order, which is important for metavariables.

```yaml
all:
  - kind: call_expression
  - pattern: console.log($ARG)
```

### `any`: Disjunction of Rules

This matches a node if any sub-rules in the list match.

```yaml
any:
  - pattern: console.log($ARG)
  - pattern: console.warn($ARG)
  - pattern: console.error($ARG)
```

### `not`: Negation of a Rule

This matches a node if the single sub-rule does not match.

```yaml
not:
  pattern: console.log($ARG)
```

### `matches`: Rule Reuse and Utility Rules

This takes a rule ID string and matches if the referenced utility rule matches.
It enables rule reuse and recursive rules.

## Metavariables

Metavariables are placeholders in patterns to match dynamic content in the AST.

### `$VAR`: Single Named Node Capture

This captures a single named node in the AST.

- Valid: `$META`, `$META_VAR`, `$_`
- Invalid: `$invalid`, `$123`, `$KEBAB-CASE`
- Example: `console.log($GREETING)` matches `console.log('Hello World')`
- Reuse: `$A == $A` matches `a == a` but not `a == b`

### `$$VAR`: Single Unnamed Node Capture

This captures a single unnamed node, such as an operator or punctuation.

Example:

```yaml
rule:
  kind: binary_expression
  has:
    field: operator
    pattern: $$OP
```

### `$$$MULTI_META_VARIABLE`: Multi-Node Capture

This matches zero or more AST nodes in a non-greedy way. It is useful for
variable numbers of arguments or statements.

- Example: `console.log($$$)` matches `console.log()`, `console.log('hello')`,
  and `console.log('debug:', key, value)`
- Example: `function $FUNC($$$ARGS) { $$$ }` matches functions with varying
  parameters or statements

### Non-Capturing Metavariables with `_VAR`

Metavariables starting with an underscore are not captured. They can match
different content even if named identically, which can improve performance.

- Example: `$_FUNC($_FUNC)` matches `test(a)` and `testFunc(1 + 1)`

### Important Considerations for Metavariable Detection

- Syntax matching only recognizes exact metavariable syntax such as `$A`, `$$B`,
  or `$$$C`
- Metavariable text must be the only text within its AST node
- Non-working examples include `obj.on$EVENT`, `"Hello $WORLD"`, `a $OP b`, and
  `$jq`

The ast-grep playground is useful for debugging patterns and visualizing
metavariables.

## Common Patterns and Examples

### Finding Functions with Specific Content

Find functions that contain `await` expressions:

```yaml
rule:
  kind: function_declaration
  has:
    pattern: await $EXPR
    stopBy: end
```

### Finding Code Inside Specific Contexts

Find `console.log` calls inside class methods:

```yaml
rule:
  pattern: console.log($$$)
  inside:
    kind: method_definition
    stopBy: end
```

### Combining Multiple Conditions

Find async functions that use `await` but do not have `try-catch`:

```yaml
rule:
  all:
    - kind: function_declaration
    - has:
        pattern: await $EXPR
        stopBy: end
    - not:
        has:
          pattern: try { $$$ } catch ($E) { $$$ }
          stopBy: end
```

### Matching Multiple Alternatives

Find any type of `console` method call:

```yaml
rule:
  any:
    - pattern: console.log($$$)
    - pattern: console.warn($$$)
    - pattern: console.error($$$)
    - pattern: console.debug($$$)
```

## Troubleshooting Tips

1. Rule does not match: use `dump_syntax_tree` to see the actual AST structure
2. Relational rule issues: ensure `stopBy: end` is set for deep searches
3. Wrong node kind: check the language's Tree-sitter grammar for correct kind
   names
4. Metavariable not working: ensure it is the only content in its AST node
5. Pattern too complex: break it down into simpler sub-rules using `all`
