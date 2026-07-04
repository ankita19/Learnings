# Tiny RAG Example (Python + Claude)

A minimal RAG demo for learning. It shows the core loop in plain Python:

**retrieve → augment → generate**

1. **retrieve** – find the docs most relevant to the question (simple word overlap)
2. **augment** – put those docs into the prompt as "context"
3. **generate** – ask Claude to answer using only that context

## Run it

```bash
pip install anthropic
# PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-..."
python rag_example.py
```

## How it maps to a real system

| In `rag_example.py` | Real production version |
|---|---|
| `retrieve()` (word overlap) | embedding model + vector DB (cosine search) |
| `DOCUMENTS` dict | your files / database / web pages |
| `answer()` | the same RAG prompt to the LLM |

Once you understand this, the cookbook's **Contextual Retrieval** is just a
smarter `retrieve()` step — see
`../claude-cookbooks/capabilities/contextual-embeddings/FLOW.md`.

> Uses `claude-opus-4-8`. Swap the model string in `rag_example.py` for a
> different one (e.g. `claude-haiku-4-5` for speed).
