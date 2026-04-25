---
name: openapi-inspection
description: Agent Skill for inspecting OpenAPI specs. Use before making REST API calls. This skill is usually invoked by other skills, commands or tasks, but user can also directly invoke this skill for other purposes.
---

# OpenAPI Inspection

- Fetch the spec using `curl` into a temp directory.
- Avoid reading the whole spec. Use `yq`/`rg` to search for relevant endpoints,
  parameters, request bodies, responses, and related schemas.

## Safety And Context Rules

- Do not invent endpoints, fields, enum values, or server URLs. Verify them from
  the spec or label them as caller-provided assumptions.
- If the spec is ambiguous, inspect adjacent tags, operation summaries, and
  schemas before choosing an endpoint.
- If multiple endpoints could satisfy the goal, use the best candidates and
  explain the tradeoff briefly.
- If the spec cannot be fetched or parsed, report the command attempted, the
  failure, and the next concrete thing that can be done.
