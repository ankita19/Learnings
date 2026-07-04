# 15-Day Interview Prep — Senior/Principal AI & Data Roles
> Built: 2026-06-22 | ~2 hrs/day | Target roles below
> Philosophy: **You are not a hardcore-SWE candidate. Don't prep like one.**
> System design + AI depth + executive storytelling are the main event. Coding is daily *insurance* — enough to not fail a screen, not enough to win on. ML-modeling depth (training/RLHF/fine-tuning) is explicitly OUT of scope — your top targets don't gate on it.

---

## Target Roles (ranked by ease-to-crack for your profile)

| Priority | Role | What its loop actually tests | Your status |
|---|---|---|---|
| **1** | WF — Principal Eng, AI Platforms | AI/agentic system design, responsible-AI/risk, **executive storytelling**, light coding | Over-qualified on YoE; ⚠️ check visa sponsorship |
| **2** | Airbnb — Sr Staff DE, Data Stewardship | Data governance strategy, quality-at-scale, architecture, change mgmt. **No coding gauntlet** | Governance + scale + leadership confirmed |
| **3** | Airbnb — Staff SWE, Data Engineering | Distributed pipeline system design + data modeling + **one coding round** | Purest fit; coding is the only gap |

> Your confirmed profile: 10+ yrs, distributed-scale DE (Spark/Kafka), 5+ yrs cross-team leadership, led governance/quality programs, edge in AI evals/RAG/agents. Gaps: algo coding under pressure, ML-fundamentals depth.

---

## Daily Structure (~2 hrs)

| Block | Time | What |
|---|---|---|
| **Coding warm-up** | 20 min | One pattern, typed from scratch, no autocomplete. Builds muscle memory for your weak round. |
| **Deep work** | 70 min | Today's main topic — **speak it out loud first**, then write/diagram |
| **Narration drill** | 20 min | Re-explain today's topic in 3 min as if to an interviewer. Record yourself. |
| **Log** | 10 min | One line: what would trip you in an interview tomorrow |

> **Non-negotiable:** the narration drill. Your interviews are won by *talking* clearly (system design, storytelling), not by silent correctness. This is the highest-ROI 20 min of your day.

---

## Coding Warm-Up Rotation (20 min/day — insurance only)

Reuse your existing `interview_prep_plan.md` unified templates + `blind75_skeletons.md`. One per day, **type it cold, then retype from scratch once**. Goal: clear a *medium*, cleanly. Do NOT chase hards.

| Day | Pattern (from your existing templates) |
|---|---|
| 1 | HashMap — Two Sum / frequency count |
| 2 | HashMap — Group Anagrams |
| 3 | Two Pointers — Valid Palindrome |
| 4 | Two Pointers — Container With Most Water |
| 5 | Sliding Window — Longest Substring (Q1/Q2/Q3 framework) |
| 6 | Sliding Window — Min Window Substring |
| 7 | BFS — Level Order Traversal |
| 8 | BFS/DFS — Number of Islands (grid) |
| 9 | Heap — Top K Frequent (bucket sort recall) |
| 10 | Intervals — Merge Intervals |
| 11 | Re-drill your 2 weakest from days 1–10 |
| 12 | Re-drill your 2 next-weakest |
| 13 | Mixed: pick 2 at random, 25 min total (timed) |
| 14 | Mixed: pick 2 at random, 25 min total (timed) |
| 15 | One easy, clean, no bugs — confidence close |

---

## Phase 1 — Days 1–2: Setup + Story Inventory

### Day 1 — Map yourself to the roles + visa check
- Confirm WF visa sponsorship situation (gating for #1).
- Write a 1-page "evidence sheet": for each target, list 2–3 real projects from your career that prove the requirement. This becomes your behavioral fuel.
- Deep work: list every system you've designed/scaled. Pick your **3 strongest** — these become your hero stories.

### Day 2 — STAR story skeletons (Principal/Staff level)
Draft 5 STAR stories (Situation→Task→Action→Result, numbers in the Result):
1. **Technical leadership** — an AI/data system you designed end-to-end
2. **Influence without authority** — aligned multiple teams/execs on a technical direction
3. **Ambiguity** — scoped a vague AI/data initiative into a shipped system
4. **Governance/quality** — a data quality/governance program you led (Stewardship gold)
5. **Disagreement** — pushed back on a technical decision; what happened

> These 5 cover ~80% of Principal/Staff behavioral rounds across all 3 targets.

---

## Phase 2 — Days 3–7: System Design (your biggest lever)

Use this framework for **every** design (write it as headers, fill each):
```
1. Clarify   → functional + non-functional (scale, latency, cost, SLA), constraints
2. Architecture → draw boxes first: source → ingest → process → store → serve
3. Key decisions → name the tradeoff at each box, state YOUR opinion + why
4. Quality/observability → how you know it works; what you monitor/alert on
5. Failure modes → what breaks at scale, how you mitigate
```

| Day | Design prompt | Maps to |
|---|---|---|
| 3 | **Enterprise data platform at PB scale** — batch + real-time, Spark/Kafka, data modeling | Airbnb Staff DE |
| 4 | **Data governance & quality system** — lineage, catalog, quality checks, GDPR/compliance, change mgmt across org | Airbnb Stewardship |
| 5 | **Agentic AI platform** — agent framework, orchestration (LangGraph), tool use, memory, RAG, model gateway | WF + Amex |
| 6 | **LLM evaluation & observability platform** — golden sets, LLM-as-judge, regression testing, offline↔online, safety/guardrails | WF + your edge |
| 7 | **Reusable AI platform for an enterprise** (WF's literal ask) — responsible AI, AI risk, autonomy boundaries, cost/safety tradeoffs | WF Principal |

> For each: do the design, then the **narration drill is the real test** — can you walk a "senior leader" through it in 5 min with crisp tradeoffs? This is "executive technical storytelling," which WF tests explicitly.

---

## Phase 3 — Days 8–10: AI / Agentic Depth (sharpen your edge)

Be able to explain each in 2 min, with an opinion. (Pull from `staff_ai_engineer_prep_plan.md`, but **skip the ML-modeling-heavy weeks** — RLHF/DPO/training internals are not required by your top targets.)

| Day | Topics |
|---|---|
| 8 | **Agents:** single vs multi-agent, ReAct vs plan-execute vs function calling, tool design, memory (episodic/semantic), when agents loop/fail + guardrails |
| 9 | **RAG + retrieval:** chunking strategies, dense vs sparse vs hybrid, reranking, grounding, why naive RAG fails; **frameworks: when to use LangChain/LlamaIndex vs lightweight primitives** |
| 10 | **Evaluation + responsible AI:** offline↔online alignment, golden sets, synthetic data, LLM-as-judge (+ its failure modes), drift/bias, hallucination/PII/safety, AI risk in regulated finance |

> Day 10 is your strongest material (evals + governance + regulated context). Over-prepare it — it's where you out-shine other candidates at WF/Amex/Airbnb-Eval.

---

## Phase 4 — Days 11–12: Behavioral + Executive Storytelling

### Day 11 — Polish the 5 STAR stories
- Tighten each to: Situation/Task in 2 sentences, Action = most of it, Result = numbers.
- Narration drill: deliver each in 90 seconds, out loud, recorded. Listen back for rambling.

### Day 12 — Executive translation drill
- For each hero system, prepare **two versions**: keyboard-level (deep technical) and exec-level (business impact, one diagram, no jargon). WF tests both in the same loop.
- Practice the pivot: interviewer says "explain to a non-technical VP" → switch registers cleanly.

---

## Phase 5 — Days 13–15: Mocks + Consolidation

### Day 13 — Mock: System Design (60 min, recorded)
- Pick one prompt you haven't drilled (e.g., "design real-time competitive-pricing data system"). Full 5-step framework, out loud, timed. Review: where did you go vague or silent?

### Day 14 — Mock: Behavioral + Coding (60 min)
- 30 min: 4 behavioral questions, cold, recorded.
- 30 min: 2 medium coding problems, timed, no help. Note the exact moment you slowed.

### Day 15 — Consolidation (no new material)
- Re-skim all 5 system-design frameworks + 5 STAR stories from memory.
- One clean easy coding problem.
- **Stop. You're prepping to feel ready, not cramped.**

---

## What to DELIBERATELY skip (protect your time)
- ❌ Hard DP, graph algorithms, competitive-programming patterns — not your roles, not your strength.
- ❌ ML model internals: backprop, training loops, RLHF/PPO/DPO, fine-tuning math — your top targets don't gate on it; "familiarity" framing only.
- ❌ Product-DS stats (causal inference, power analysis) — only relevant to the Advanced Analytics role you're skipping.

## Weak-Areas Log
> Add a line every time you blank or stumble. Review before each session.

---

## Progress Tracker

| Day | Focus | Coding warm-up | Done |
|---|---|---|---|
| 1 | Role mapping + visa check | HashMap (Two Sum) | [ ] |
| 2 | STAR story skeletons | HashMap (Anagrams) | [ ] |
| 3 | SD: data platform @ scale | Two Pointers (Palindrome) | [ ] |
| 4 | SD: governance/quality | Two Pointers (Container) | [ ] |
| 5 | SD: agentic AI platform | Sliding Window (Longest) | [ ] |
| 6 | SD: eval/observability | Sliding Window (Min Window) | [ ] |
| 7 | SD: reusable AI platform (WF) | BFS (Level Order) | [ ] |
| 8 | AI depth: agents | BFS/DFS (Islands) | [ ] |
| 9 | AI depth: RAG/retrieval | Heap (Top K) | [ ] |
| 10 | AI depth: eval/responsible AI | Intervals (Merge) | [ ] |
| 11 | Behavioral: STAR polish | Re-drill weakest 2 | [ ] |
| 12 | Exec storytelling | Re-drill next 2 | [ ] |
| 13 | Mock: system design | Timed mixed 2 | [ ] |
| 14 | Mock: behavioral + coding | Timed mixed 2 | [ ] |
| 15 | Consolidation | One clean easy | [ ] |
