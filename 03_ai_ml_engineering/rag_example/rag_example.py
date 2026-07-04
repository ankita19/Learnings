"""
A tiny RAG (Retrieval-Augmented Generation) example with Claude.

The whole idea of RAG in 4 steps:
    1. RETRIEVE   find the docs most relevant to the question
    2. AUGMENT    put those docs into the prompt as "context"
    3. GENERATE   ask Claude to answer using only that context

Setup:
    pip install anthropic
    set ANTHROPIC_API_KEY (PowerShell: $env:ANTHROPIC_API_KEY="sk-ant-...")
    python rag_example.py
"""

import anthropic

# 1. Our "knowledge base" - just a few short documents.
DOCUMENTS = {
    "prompt_caching": (
        "Prompt caching reuses a large, stable prefix across requests. "
        "Cache reads cost about 1/10th of normal input price, so a big shared "
        "prompt can cut input costs by up to ~90%. Any change to the prefix "
        "invalidates the cache."
    ),
    "contextual_retrieval": (
        "In basic RAG, each chunk is embedded alone and loses the context of "
        "its document. Contextual Retrieval uses Claude to add a short blurb "
        "describing where the chunk sits in the document before embedding it. "
        "This improved retrieval from about 87% to 95% on a benchmark."
    ),
    "tool_use": (
        "Tool use lets Claude call functions you define. You send tools with "
        "JSON schemas, Claude replies with a tool_use block, you run the tool "
        "and send back a tool_result. The SDK can run this loop for you."
    ),
}


def retrieve(question, k=2):
    """Step 1: return the k documents that share the most words with the question.

    This is a deliberately simple stand-in for a real vector search.
    """
    words = set(question.lower().split())
    scored = []
    for doc_id, text in DOCUMENTS.items():
        overlap = len(words & set(text.lower().split()))
        scored.append((overlap, doc_id, text))
    scored.sort(reverse=True)          # highest overlap first
    return scored[:k]


def answer(client, question):
    # Step 1: retrieve
    top = retrieve(question)

    # Step 2: augment - build a context block from the retrieved docs
    context = "\n\n".join(f"[{doc_id}] {text}" for _, doc_id, text in top)

    # Step 3: generate - ask Claude to answer using only that context
    response = client.messages.create(
        model="claude-opus-4-8",
        max_tokens=512,
        system=(
            "Answer the question using ONLY the context provided. "
            "If the answer isn't in the context, say so. "
            "Cite the source id in brackets, like [prompt_caching]."
        ),
        messages=[
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"}
        ],
    )

    # The response can have several blocks; grab the text one.
    return response.content[0].text


def main():
    client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

    question = "How does contextual retrieval improve search?"
    print("Q:", question)
    print()
    print(answer(client, question))


if __name__ == "__main__":
    main()
