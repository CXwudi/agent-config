---
name: linear
description: Agent Skill for Linear via GraphQL API. Use when interacting with Linear.
compatibility: Requires network access to the Linear API and curl.
---

# Linear

## Prerequisites

Requires Linear personal API key from environment variable `LINEAR_API_KEY`. If not set, ask the user to provide it.

Authenticate requests using `Authorization: ${LINEAR_API_KEY}`, do not use the `Bearer` prefix.

## Usage

Use the `graphql-inspection` skill to inspect Linear's published GraphQL schema:

`https://raw.githubusercontent.com/linear/linear/refs/heads/master/packages/sdk/src/schema.graphql`

Then send GraphQL queries or mutations via POST to `https://api.linear.app/graphql` with `Content-Type: application/json`, following the schema.

## Note

See the [official API documentation](https://linear.app/developers/graphql.md) for more details
