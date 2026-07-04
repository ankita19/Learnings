# MCP Foundations

## What MCP Is

MCP is a protocol that lets a host application discover and invoke tools exposed by a server.

- Host examples: AI apps, IDE assistants, agent runtimes
- Server examples: local process, VM service, containerized app, Kubernetes service

## Core Roles

- User: asks in natural language
- Host: decides whether to call tools and with what arguments
- MCP Server: exposes tools and executes calls
- Tool: business function with a stable input/output contract

## Correct Mental Model

- MCP server does not need to be started by the host in all deployments.
- In local stdio mode, host often starts it.
- In always-on service mode, host only connects.

## Transport Modes

- Stdio: easiest for local development and desktop tooling
- Network service: used for shared or production deployments with auth, TLS, and observability

## Practical Principle

Treat tools as API endpoints with strict contracts, versioning, and governance.
