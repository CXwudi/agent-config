---
name: graphql-inspection
description: Agent Skill for inspecting GraphQL schemas. Use before making GraphQL API calls. This skill is usually invoked by other skills, commands or tasks, but user can also directly invoke this skill for other purposes.
---

# GraphQL Inspection

- Fetch the published schema using `curl` into a temp directory
- Avoid reading the whole schema. Identify whether it is SDL (`.graphql`) or JSON introspection.
- For SDL (`.graphql`), use `rg` to locate relevant definitions, then read only those sections.
- For JSON introspection (`.json`), use `yq`/`rg` to inspect relevant types and fields.
- Look for Schema metadata to understand the input and output shapes.

## Safety And Context Rules

- Do not invent endpoint URLs, authentication requirements, fields, arguments, types, or enum values. Verify them from the schema, or label them as caller-provided assumptions.
- If the schema is ambiguous, inspect descriptions, related types, or even find and consult official documentation before choosing an operation.
- If multiple operations could satisfy the goal, use the best candidates and explain the tradeoff briefly.
- Inspect the response's `errors` as well as `data`; GraphQL errors can occur even with HTTP 200.
- If the schema cannot be fetched, queried, or parsed, report the command attempted with credentials redacted, the failure, and the next concrete thing that can be done.
