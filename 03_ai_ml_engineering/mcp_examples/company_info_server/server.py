"""Minimal MCP server with one tool: get_company_info.

Run with stdio transport (most common for local MCP hosts):
    python server.py
"""

from mcp.server.fastmcp import FastMCP


mcp = FastMCP("company-info-server")


@mcp.tool()
def get_company_info(company_name: str) -> dict:
    """Return mock company profile data for demo purposes."""

    lookup = {
        "teradata": {
            "name": "Teradata",
            "industry": "Enterprise data and AI platform",
            "headquarters": "San Diego, California, USA",
            "core_products": [
                "Teradata Vantage",
                "AI Studio",
                "Enterprise Vector Store",
            ],
            "note": "Mock payload from MCP tool",
        },
        "microsoft": {
            "name": "Microsoft",
            "industry": "Cloud, software, and AI",
            "headquarters": "Redmond, Washington, USA",
            "core_products": ["Azure", "Microsoft 365", "Dynamics 365"],
            "note": "Mock payload from MCP tool",
        },
    }

    key = company_name.strip().lower()
    return lookup.get(
        key,
        {
            "name": company_name,
            "industry": "Unknown",
            "headquarters": "Unknown",
            "core_products": [],
            "note": "No mock profile found. Try 'Teradata' or 'Microsoft'.",
        },
    )


if __name__ == "__main__":
    mcp.run(transport="stdio")
