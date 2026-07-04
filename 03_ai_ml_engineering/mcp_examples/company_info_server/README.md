# Simple MCP Service Example: Company Info Tool

This is a minimal end-to-end MCP server example with one tool:

- `get_company_info(company_name: str) -> dict`

It returns mocked company metadata (for example, `Teradata`, `Microsoft`).

## 1. Install dependencies

```bash
pip install mcp
```

## 2. Run server

```bash
python server.py
```

This starts the MCP server on `stdio` transport (local process mode).

## 3. Hook into an MCP host/client

Typical local host setup points to this command:

```json
{
  "mcpServers": {
    "company-info": {
      "command": "python",
      "args": [
        "c:/Users/ankitjai/work/personal/03_ai_ml_engineering/mcp_examples/company_info_server/server.py"
      ]
    }
  }
}
```

## 4. Example tool call

Tool name:

- `get_company_info`

Arguments:

```json
{
  "company_name": "Teradata"
}
```

Example response:

```json
{
  "name": "Teradata",
  "industry": "Enterprise data and AI platform",
  "headquarters": "San Diego, California, USA",
  "core_products": [
    "Teradata Vantage",
    "AI Studio",
    "Enterprise Vector Store"
  ],
  "note": "Mock payload from MCP tool"
}
```

## Notes

- MCP server can run anywhere your host can reach: local process, VM, Kubernetes, or managed container runtime.
- `stdio` is easiest for local development.
- For shared environments, move to network transport and add auth, TLS, and request auditing.
