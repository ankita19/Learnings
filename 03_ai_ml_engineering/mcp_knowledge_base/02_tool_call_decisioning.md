# Tool Call Decisioning

## POC Pattern Used Here

The POC router uses rule-based checks and regex extraction.

- Deterministic
- Easy to debug
- Good for narrow intents

## Real-World Patterns

### Pattern 1: LLM-native tool selection

How it works:

- Host sends user prompt plus available tool schemas to the model.
- Model returns a structured tool call (tool name plus JSON arguments).
- Host validates policy and input schema, then executes the tool.
- Tool result is passed back to model for final response composition.

Why teams use it:

- Handles natural language variation better than regex-only routing.
- Reduces brittle intent logic for large tool catalogs.

What must still be enforced:

- Authorization and tool allowlists per user or tenant.
- Argument schema validation before execution.
- Timeout and retry policy per tool.
- Tracing and auditability for every tool call.

Mock implementation in this workspace:

- Function: `mock_llm_select_tool` in `minimal_mcp_user_call_poc/app.py`
- Flow: `handle_user_prompt_with_mock_llm` -> select tool -> execute `get_company_info`

Example mock flow:

- User prompt: `get me Teradata company info`
- Mock LLM output: `{ "name": "get_company_info", "arguments": { "company_name": "teradata" } }`
- Tool result: structured company JSON payload

### Pattern 2: Hybrid routing (common in production)

- Deterministic policy checks first
- LLM chooses among allowed tools
- Better balance of control and flexibility

### Pattern 3: Pure rules engine

- High precision for fixed workflows
- Brittle as language variety grows

## Production Guardrails

- Tool allowlist by user or tenant
- Input schema validation before execution
- Confidence thresholds and clarification prompts
- Structured error taxonomy
- Request tracing and audit logs

## Design Recommendation

Use hybrid routing for enterprise workloads: policy-first, model-assisted tool selection, strict tool contracts.
