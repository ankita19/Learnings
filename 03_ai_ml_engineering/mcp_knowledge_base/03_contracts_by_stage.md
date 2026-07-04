# MCP Contracts By Stage

## Stage 1: Connection and Session Establishment

Input contract:

- transport mode
- client identity and capability flags

Output contract:

- server identity
- supported capabilities

Success:

- host confirms reachability and stores capabilities

## Stage 2: Tool Discovery

Input contract:

- tools/list request

Output contract:

- tool list with name, description, and input schema

Success:

- host can validate arguments and render tool choices

## Stage 3: Tool Invocation

Input contract:

- tool name
- structured arguments

Output contract:

- stable JSON payload
- predictable response shape

Success:

- parseable response with no schema drift

## Stage 4: Error Contract

Required fields:

- code
- message
- retryable flag
- optional details

Example codes:

- INVALID_ARGUMENT
- TOOL_NOT_FOUND
- INTERNAL_ERROR
- TIMEOUT

## Stage 5: Response Composition

Input:

- user query
- tool output
- policy constraints

Output:

- grounded user-facing answer
- no fabricated fields

Success:

- traceable output tied to tool results

## Stage 6: Operational Contract

- authentication and authorization
- observability fields such as request_id and latency
- versioning policy for tools and schemas
