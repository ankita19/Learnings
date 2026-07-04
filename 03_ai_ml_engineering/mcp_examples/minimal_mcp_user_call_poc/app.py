"""Minimal user-call POC for MCP-style tool routing.

User enters natural language.
Host/router maps intent to a tool call.
Tool executes and returns structured output.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any


_MOCK_COMPANIES: dict[str, dict[str, Any]] = {
    "teradata": {
        "name": "Teradata",
        "industry": "Enterprise data and AI platform",
        "headquarters": "San Diego, California, USA",
        "core_products": ["Teradata Vantage", "AI Studio", "Enterprise Vector Store"],
    },
    "microsoft": {
        "name": "Microsoft",
        "industry": "Cloud, software, and AI",
        "headquarters": "Redmond, Washington, USA",
        "core_products": ["Azure", "Microsoft 365", "Dynamics 365"],
    },
}

SYSTEM_INSTRUCTION = (
    "You are a tool-using assistant. For factual company profile requests, "
    "prefer calling get_company_info with a company_name argument. "
    "If the request is ambiguous, ask a clarification question."
)


@dataclass(frozen=True)
class ToolCall:
    """Represents a routed tool invocation."""

    name: str
    arguments: dict[str, Any]


@dataclass(frozen=True)
class ToolSchema:
    """Minimal tool schema shown to the mock model."""

    name: str
    description: str
    required_args: tuple[str, ...]


@dataclass(frozen=True)
class ModelDecision:
    """Mock model output after reading system instruction and tool schemas."""

    tool_call: ToolCall | None
    confidence: float
    message: str


AVAILABLE_TOOLS: tuple[ToolSchema, ...] = (
    ToolSchema(
        name="get_company_info",
        description="Return company profile facts by company name",
        required_args=("company_name",),
    ),
)


def _extract_company_name(prompt: str) -> str:
    """Extract company name from prompts ending in 'company info'."""
    match = re.search(r"(?:for|about|get me)\s+([a-zA-Z0-9 .&-]+?)\s+company\s+info", prompt)
    if match:
        return match.group(1).strip()
    # Fallback for short forms like: "teradata company info"
    return prompt.replace("company info", "").strip()


def get_company_info(company_name: str) -> dict[str, Any]:
    """Tool function with stable, predictable output shape."""
    normalized = company_name.strip().lower()
    if not normalized:
        raise ValueError("company_name must be a non-empty string")

    if normalized not in _MOCK_COMPANIES:
        return {
            "found": False,
            "name": company_name,
            "industry": "Unknown",
            "headquarters": "Unknown",
            "core_products": [],
        }

    payload = dict(_MOCK_COMPANIES[normalized])
    payload["found"] = True
    return payload


def route_user_prompt(user_prompt: str) -> ToolCall:
    """Very small intent router for company-info requests."""
    prompt = user_prompt.strip().lower()
    if not prompt:
        raise ValueError("user_prompt must be a non-empty string")

    if "company" in prompt and "info" in prompt:
        company_name = _extract_company_name(prompt)
        if not company_name:
            raise ValueError("Could not extract company name from prompt")
        return ToolCall(name="get_company_info", arguments={"company_name": company_name})

    raise ValueError("Unsupported request. Try: 'get me Teradata company info'")


def mock_llm_decide_tool(
    user_prompt: str,
    system_instruction: str = SYSTEM_INSTRUCTION,
    available_tools: tuple[ToolSchema, ...] = AVAILABLE_TOOLS,
) -> ModelDecision:
    """Mock a realistic model decision using instruction + schemas + prompt.

    This function simulates what a model returns in tool-calling mode:
    - optional tool call
    - confidence score
    - fallback/clarification message
    """
    _ = system_instruction
    tool_names = {tool.name for tool in available_tools}
    if "get_company_info" not in tool_names:
        return ModelDecision(
            tool_call=None,
            confidence=0.0,
            message="No suitable tool is available for company profile lookup.",
        )

    prompt = user_prompt.strip().lower()
    if not prompt:
        raise ValueError("user_prompt must be a non-empty string")

    if "company" in prompt and "info" in prompt:
        company_name = _extract_company_name(prompt)
        if not company_name:
            return ModelDecision(
                tool_call=None,
                confidence=0.35,
                message="I can fetch company info. Which company should I use?",
            )
        return ModelDecision(
            tool_call=ToolCall(name="get_company_info", arguments={"company_name": company_name}),
            confidence=0.94,
            message="Using company info tool for factual lookup.",
        )

    return ModelDecision(
        tool_call=None,
        confidence=0.41,
        message="I can help with company info requests like 'get me Teradata company info'.",
    )


def _validate_tool_call(tool_call: ToolCall, available_tools: tuple[ToolSchema, ...]) -> None:
    """Validate tool name and required arguments before execution."""
    schema_by_name = {tool.name: tool for tool in available_tools}
    if tool_call.name not in schema_by_name:
        raise ValueError(f"Unknown tool: {tool_call.name}")

    schema = schema_by_name[tool_call.name]
    for required_arg in schema.required_args:
        if required_arg not in tool_call.arguments:
            raise ValueError(f"Missing required argument: {required_arg}")

    company_name = tool_call.arguments.get("company_name")
    if not isinstance(company_name, str) or not company_name.strip():
        raise ValueError("company_name must be a non-empty string")


def handle_user_prompt(user_prompt: str) -> dict[str, Any]:
    """Host orchestration: route prompt -> call tool -> return result."""
    tool_call = route_user_prompt(user_prompt)

    if tool_call.name != "get_company_info":
        raise ValueError(f"Unknown tool: {tool_call.name}")

    return get_company_info(tool_call.arguments["company_name"])


def handle_user_prompt_with_mock_llm(
    user_prompt: str,
    confidence_threshold: float = 0.7,
) -> dict[str, Any]:
    """Host orchestration using realistic mock model decisioning."""
    decision = mock_llm_decide_tool(user_prompt=user_prompt)

    if decision.tool_call is None or decision.confidence < confidence_threshold:
        return {
            "needs_clarification": True,
            "message": decision.message,
            "confidence": decision.confidence,
        }

    _validate_tool_call(decision.tool_call, AVAILABLE_TOOLS)

    if decision.tool_call.name != "get_company_info":
        raise ValueError(f"Unknown tool: {decision.tool_call.name}")

    result = get_company_info(decision.tool_call.arguments["company_name"])
    return {
        "needs_clarification": False,
        "tool_used": decision.tool_call.name,
        "confidence": decision.confidence,
        "result": result,
    }


def main() -> None:
    prompt = input("Ask: ").strip()
    try:
        result = handle_user_prompt_with_mock_llm(prompt)
        print(result)
    except ValueError as exc:
        print({"error": str(exc)})


if __name__ == "__main__":
    main()
