# Agentic Orchestration Pattern (Sanitized)

This note captures a generic, production-style orchestration loop for LLM tool calling.
No vendor-specific or internal repository details are included.

## High-Level Pattern

1. A service receives a user request.
2. The service builds context (user message, conversation history, business context, system instructions).
3. The service sends messages plus tool definitions (name, description, JSON parameters) to an LLM API.
4. The LLM decides either:
   - return tool calls, or
   - return a final answer.
5. If tool calls are returned, the service executes each tool.
6. Tool results are appended to conversation history as tool-role messages.
7. The service calls the LLM again with updated context.
8. Loop continues until the LLM returns a final user-facing response.

## Generic Sequence

```text
User Request
  -> Orchestrator Service
  -> Build Context + Tool Definitions
  -> LLM API Call
  -> ToolCall[] or Final Response
  -> Execute Tool(s) if needed
  -> Append Tool Results
  -> LLM API Call (next step)
  -> Final Response to User
```

## Pseudocode

```csharp
// Generic pseudocode from an orchestrator service
while (shouldContinue) {
  // Step 1: LLM analyzes + decides what to do
  var response = await llmClient.ChatCompletionAsync(
    new ChatCompletionRequest {
      Messages = conversationHistory,
      Tools = availableTools,  // LLM sees these options
      Instructions = systemPrompt
    });

  // Step 2: Check if LLM wants to call a tool
  if (response.ToolCalls != null && response.ToolCalls.Count > 0) {
    // Step 3: Service executes the tool
    foreach (var toolCall in response.ToolCalls) {
      var tool = toolRegistry.GetTool(toolCall.Name);
      var result = await tool.ExecuteAsync(toolCall);

      // Step 4: Append result for LLM to see
      conversationHistory.Add(new {
        Role = "tool",
        ToolCallId = toolCall.Id,
        Content = result
      });
    }
    // Loop continues and LLM can decide next action
  } else {
    // LLM generated final response (no tool call)
    shouldContinue = false;
  }
}
```

## Decision Ownership

- Orchestrator service owns:
  - conversation state
  - tool registry
  - validation, authz, and policy checks
  - execution and retries
  - observability and audit logs

- LLM owns:
  - reasoning over context
  - deciding whether a tool is needed
  - choosing which tool and arguments
  - producing final response when enough evidence exists

## Three Common LLM Decisions

1. Call an information retrieval tool.
2. Call a case, analytics, or business-logic tool.
3. Stop tool use and generate final response.

## Why This Is Agentic

Traditional one-shot pattern:

- user request -> model answer

Agentic loop pattern:

- user request -> plan -> tool execution -> updated context -> adapt -> final answer

## Required Guardrails

- Tool allowlists by tenant/user role
- Argument schema validation before execution
- Timeout/retry policies per tool
- Redaction and data handling controls
- Tracing fields (request_id, tool_name, latency, status)

## Minimal Interview Talk Track

"In a production agentic system, the service orchestrates the loop and enforces policy, while the LLM acts as the decision-maker for tool selection. Tool results are fed back into context so the model can iteratively reason and decide whether to call another tool or finalize the answer."
