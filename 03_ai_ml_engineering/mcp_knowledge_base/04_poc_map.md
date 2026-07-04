# POC Map In This Workspace

## Minimal MCP Server POC

Path:

- 03_ai_ml_engineering/mcp_examples/minimal_mcp_company_info

Purpose:

- Demonstrates MCP tool declaration and execution with one tool: get_company_info

Key files:

- src/minimal_mcp_company_info/server.py
- tests/test_server.py

## User-Call Routing POC

Path:

- 03_ai_ml_engineering/mcp_examples/minimal_mcp_user_call_poc

Purpose:

- Demonstrates host-side natural-language routing to internal tool invocation

Key files:

- app.py
- tests/test_app.py

## Suggested Next Iterations

1. Connect user-call router to real MCP server transport instead of local in-process function calls.
2. Add argument schema validation layer.
3. Add auth and per-tenant tool allowlists.
4. Add structured telemetry and error codes.
