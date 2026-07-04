# Staff AI Engineer — 4 Month Interview Prep Plan
> Start: April 9, 2026 | Target: August 8, 2026
> Background: Data Engineer → AI Engineer (LLM pipelines, evaluation, agents)

---

## What Gets You Hired at Staff Level

| Track | Weight | Why |
|---|---|---|
| ML System Design | 35% | Staff = design end-to-end AI systems, not just code them |
| AI/LLM Technical Depth | 25% | Must go deeper than "I used LangChain" |
| DS/Algo Coding | 20% | Still required — but lower bar than SWE Staff |
| Data/ML Coding | 10% | SQL, pandas, maybe model training code |
| Behavioral / Leadership | 10% | Staff = cross-functional influence, not just IC work |

---

## Daily Structure (1.5 hrs/day)

| Block | Time | What |
|---|---|---|
| Cold recall | 15 min | Recreate yesterday's design/concept from memory |
| Deep work | 50 min | Today's topic — speak it first, then write |
| Transfer drill | 20 min | Apply concept to a variation |
| Log | 5 min | One sentence: what would trip you in an interview |

---

## Phase 1 — Weeks 1–4: Foundation (April 9 – May 6)

### Weeks 1–2: Complete DS/Algo (use existing algo prep plan)
Focus only on patterns most likely at Staff AI interviews:
- HashMap + Frequency count
- Sliding Window (unified template)
- BFS/DFS on graphs/grids
- Two pointers

> Skip: hard DP, segment trees, advanced graph algorithms — low ROI for this role.

### Week 3: Transformer + LLM Internals
You use LLMs daily. Now explain them at depth.

**Must be able to explain:**
- Attention mechanism — what Q, K, V actually are
- Why positional encoding? What breaks without it?
- How context window works — and why longer = more expensive
- Tokenization — why "ChatGPT" ≠ one token
- Temperature, top-p, top-k — what they control and when to use each
- Why fine-tuning changes behavior vs prompt engineering

**Practice format:** explain each concept in 2 minutes out loud, no notes.

### Week 4: Embeddings + Vector Search
Your data engineering background helps here — think of this as a new type of index.

**Must be able to explain:**
- What an embedding is and why similar things are close
- Cosine similarity vs dot product vs L2 — when to use which
- How HNSW index works (approximate nearest neighbour)
- Vector DB comparison: Pinecone vs Weaviate vs pgvector vs Chroma
- Chunking strategies: fixed, semantic, hierarchical
- Why naive chunking breaks retrieval

---

## Phase 2 — Weeks 5–10: ML System Design (May 7 – June 17)

> This is the highest-weight track. Spend the most energy here.

### The ML System Design Framework (use for every problem)

```
1. Clarify requirements
   - Functional: what does it do?
   - Non-functional: latency, scale, cost, accuracy target?
   - Constraints: data available? model size limit? real-time vs batch?

2. High-level architecture
   - Data flow: input → retrieval/processing → model → output
   - Draw the boxes before explaining any one box

3. Model selection
   - Why this model? What are the tradeoffs?
   - Open source vs API? Fine-tuned vs prompted?

4. Evaluation strategy
   - How do you know it works? Offline metrics + online metrics
   - What does failure look like?

5. Production concerns
   - Latency: where are the bottlenecks?
   - Cost: what's expensive and how do you reduce it?
   - Safety: hallucination, PII, toxicity
   - Monitoring: what do you alert on?
```

### Week 5–6: RAG System Design

**The canonical Staff interview question.**

**Design a RAG system for [enterprise knowledge base / customer support / internal docs]**

Key decisions you must have opinions on:
- Chunking: size, overlap, strategy (fixed vs semantic)
- Embedding model: OpenAI ada vs sentence-transformers vs domain-specific
- Retrieval: dense vs sparse (BM25) vs hybrid
- Reranking: why, when, cross-encoder vs bi-encoder
- Context assembly: how do you fit retrieved chunks into the prompt?
- Answer generation: which model, what prompt template
- Evaluation: RAGAS metrics — faithfulness, answer relevancy, context precision/recall

**Practice problem:** Design a RAG system for a 500-person company's internal HR policy docs. Latency target: < 3s. 10K queries/day.

**Practice problem:** How would you define the orchestration layer in a GenAI and agent-based reference architecture for advisor assist workflows at Vanguard, and what critical considerations would you emphasize in its design to ensure it aligns with existing advice and wealth management systems?

### Week 7–8: AI Agent System Design

**Design an AI agent that [books meetings / writes code / handles customer tickets]**

Key decisions:
- Single agent vs multi-agent — when to split?
- Tool design: what tools does the agent have? How are they defined?
- Planning: ReAct vs Plan-and-Execute vs function calling
- Memory: in-context vs external (episodic, semantic, procedural)
- Error handling: what happens when a tool fails or LLM loops?
- Human-in-the-loop: when to escalate?
- Evaluation: task completion rate, step accuracy, cost per task

**Practice problem:** Design a customer support agent for a SaaS product that can look up account info, reset passwords, and escalate to a human. Handle 50K tickets/day.

### Week 9–10: Evaluation + MLOps for AI Systems

**The gap most AI engineers have. Your background gives you a head start.**

**Evaluation:**
- Offline: RAGAS, G-Eval, MT-Bench, human eval — tradeoffs of each
- Online: A/B testing LLMs, shadow deployment, canary releases
- Metrics: faithfulness, relevance, groundedness, toxicity, latency
- Golden dataset: how to build and maintain one

**MLOps for LLM systems:**
- Prompt versioning — treating prompts like code
- Experiment tracking (MLflow, W&B, LangSmith)
- Model registry and deployment patterns
- Observability: token usage, latency, error rates, cost per query
- Fine-tuning pipeline: data prep → training → evaluation → deployment

---

## Phase 3 — Weeks 11–14: AI Technical Depth (June 18 – July 15)

### Week 11: Fine-Tuning + Alignment
- When to fine-tune vs prompt engineer vs RAG (the decision tree)
- LoRA / QLoRA — why low-rank, what you actually change
- RLHF — reward model, PPO, why it's expensive
- DPO — simpler alternative to RLHF, how it works
- PEFT methods overview

**Interview question:** "When would you fine-tune vs use RAG? Walk me through the decision."

### Week 12: Production AI Systems
- Inference optimization: quantization (INT4, INT8), KV cache, speculative decoding
- Serving: vLLM, TGI, Triton — when to use each
- Cost optimization: caching, batching, model routing (small model first)
- Latency: TTFT vs TPOT — what users actually feel
- Context management: sliding window, summarization, selective retention

### Week 13: Data Engineering for AI (your edge)
This is where your background becomes a differentiator — most AI engineers are weak here.

- Feature stores for ML: offline vs online, point-in-time correctness
- Training data pipelines: deduplication, quality filtering, PII scrubbing
- Data flywheel: how production traffic improves the model
- Synthetic data generation: when and how
- Embedding pipelines at scale: batch vs streaming, incremental updates

### Week 14: First Full Mock Interviews
- 1 full ML system design (60 min) — record yourself
- 1 DS/algo round (45 min) — timed, no help
- Review: where did you slow down? What did you not have an opinion on?

---

## Phase 4 — Weeks 15–17: Mock + Polish (July 16 – August 8)

### Week 15–16: Mock Loops
- 2 full mock system design sessions per week
- 2 algo sessions per week
- 1 behavioral session per week

### Week 17: Target Company Specific
- Research each company's AI stack (public eng blogs, papers, GitHub)
- Align your experience to their problems
- Prepare 3 STAR stories: led ambiguous AI project, disagreed on technical direction, delivered under constraint

---

## Behavioral — Staff Level (ongoing, 20 min/week)

Staff interviews test influence, not just execution. Prepare answers for:

| Theme | Question type |
|---|---|
| Technical leadership | "Tell me about an AI system you designed end-to-end" |
| Ambiguity | "How did you scope an AI project with unclear requirements?" |
| Disagreement | "When did you push back on a technical direction? What happened?" |
| Scale | "How did you make an AI system reliable at production scale?" |
| Cross-functional | "How did you align non-technical stakeholders on an AI decision?" |

**STAR format:** Situation (1 sentence) → Task (1 sentence) → Action (most of the time) → Result (numbers where possible)

---

## Weak Areas Log

> Add every time you get stuck or blank. Review before every session.

---

## Progress Tracker

### Phase 1 — Foundation

| Week | Topic | Done | Notes |
|---|---|---|---|
| 1–2 | DS/Algo completion | [ ] | |
| 3 | Transformer + LLM internals | [ ] | |
| 4 | Embeddings + Vector search | [ ] | |

### Phase 2 — ML System Design

| Week | Topic | Done | Notes |
|---|---|---|---|
| 5–6 | RAG system design | [ ] | |
| 7–8 | AI Agent system design | [ ] | |
| 9–10 | Evaluation + MLOps | [ ] | |

### Phase 3 — Technical Depth

| Week | Topic | Done | Notes |
|---|---|---|---|
| 11 | Fine-tuning + Alignment | [ ] | |
| 12 | Production AI systems | [ ] | |
| 13 | Data engineering for AI | [ ] | |
| 14 | First full mocks | [ ] | |

### Phase 4 — Mock + Polish

| Week | Topic | Done | Notes |
|---|---|---|---|
| 15–16 | Full mock loops | [ ] | |
| 17 | Company-specific prep | [ ] | |

---

## Resources

| Topic | Resource |
|---|---|
| DS/Algo | NeetCode (existing subscription) |
| LLM internals | Andrej Karpathy — "Let's build GPT" (YouTube) |
| RAG | LangChain docs + RAGAS docs |
| ML System Design | "Designing ML Systems" — Chip Huyen (book) |
| LLM Evaluation | RAGAS paper, G-Eval paper |
| Fine-tuning | HuggingFace PEFT docs, Sebastian Raschka blog |
| Production LLMs | vLLM docs, "LLM in Production" (YouTube talks) |
| Behavioral | "Staff Engineer" — Will Larson (book) |
