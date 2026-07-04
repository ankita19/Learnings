# Minimal MCP Company Info

A minimal Python MCP server POC with one tool:

- `get_company_info(company_name: str)`

## Quick start

```bash
python -m venv .venv
. .venv/Scripts/activate
pip install -e .
python -m minimal_mcp_company_info.server
```

The server runs on stdio transport for local MCP hosts.

## Tool contract

Input:

```json
{
  "company_name": "Teradata"
}
```

Output:

```json
{
  "found": true,
  "name": "Teradata",
  "industry": "Enterprise data and AI platform",
  "headquarters": "San Diego, California, USA",
  "core_products": ["Teradata Vantage", "AI Studio", "Enterprise Vector Store"]
}
```

## Run tests

```bash
python -m unittest discover -s tests -p "test_*.py"
```
