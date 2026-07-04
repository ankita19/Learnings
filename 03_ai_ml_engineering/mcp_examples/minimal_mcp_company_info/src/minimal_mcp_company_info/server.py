"""Minimal MCP server exposing one tool for company info."""

from __future__ import annotations

from copy import deepcopy
from typing import Any

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("minimal-company-info")

_MOCK_COMPANIES: dict[str, dict[str, Any]] = {
    "teradata": {
        "name": "Teradata",
        "industry": "Enterprise data and AI platform",
        "headquarters": "San Diego, California, USA",
        "core_products": [
            "Teradata Vantage",
            "AI Studio",
            "Enterprise Vector Store",
        ],
    },
    "microsoft": {
        "name": "Microsoft",
        "industry": "Cloud, software, and AI",
        "headquarters": "Redmond, Washington, USA",
        "core_products": ["Azure", "Microsoft 365", "Dynamics 365"],
    },
}


def _normalize_company_name(company_name: str) -> str:
    """Normalize input so lookups are consistent and predictable."""
    return company_name.strip().lower()


@mcp.tool()
def get_company_info(company_name: str) -> dict[str, Any]:
    """Return mock company info by company name."""
    normalized_name = _normalize_company_name(company_name)
    if not normalized_name:
        raise ValueError("company_name must be a non-empty string")

    if normalized_name not in _MOCK_COMPANIES:
        return {
            "found": False,
            "name": company_name,
            "industry": "Unknown",
            "headquarters": "Unknown",
            "core_products": [],
        }

    payload = deepcopy(_MOCK_COMPANIES[normalized_name])
    payload["found"] = True
    return payload


if __name__ == "__main__":
    mcp.run(transport="stdio")
