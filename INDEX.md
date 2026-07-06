# Learnings — Study Index

> Last Updated: 2026-07-06
> Use this page as your single entry point for all study material.

---

## 01 — Coding / DSA

| File | What it is |
|---|---|
| [blind75_skeletons.md](01_coding_dsa/blind75_skeletons.md) | Blind 75 problem list with solution skeletons |
| [dsa_warmup_templates.py](01_coding_dsa/dsa_warmup_templates.py) | Reusable warm-up templates: arrays, hashmap, heap, BFS/DFS, binary search |
| [code_snip_practice.py](01_coding_dsa/code_snip_practice.py) | Quick code snippets for practice |

**Practice problems (`01_coding_dsa/practice/`):**

| File | Topic |
|---|---|
| [ds_algo.py](01_coding_dsa/practice/ds_algo.py) | Core data structures |
| [KthLargestRunningStream.py](01_coding_dsa/practice/KthLargestRunningStream.py) | Heap / running stream |
| [LRUCache.py](01_coding_dsa/practice/LRUCache.py) | LRU Cache implementation |
| [MergeInterval.py](01_coding_dsa/practice/MergeInterval.py) | Merge intervals |
| [ProductOfArray.py](01_coding_dsa/practice/ProductOfArray.py) | Product of array except self |
| [sliding_window.py](01_coding_dsa/practice/sliding_window.py) | Sliding window pattern |
| [TopK.py](01_coding_dsa/practice/TopK.py) | Top-K elements |
| [reverse_words.py](01_coding_dsa/practice/reverse_words.py) | String manipulation |
| [vote_counter.py](01_coding_dsa/practice/vote_counter.py) | Vote counter |

---

## 02 — Python / Data Engineering

| File | What it is |
|---|---|
| [python_de_prep.md](02_python_data_eng/python_de_prep.md) | Python + data engineering interview prep notes |
| [python_notebook.ipynb](02_python_data_eng/notebooks/python_notebook.ipynb) | Python concepts notebook |
| [ds_notebook.ipynb](02_python_data_eng/notebooks/ds_notebook.ipynb) | Data science notebook |

---

## 03 — AI / ML Engineering

### GenAI System Architecture

| File | What it is |
|---|---|
| [GenAI_System_Architecture_Learning_Guide.md](03_ai_ml_engineering/GenAI_System_Architecture_Learning_Guide.md) | ⭐ Main study guide — 5 modules, 22 topics, interview answers, templates |
| [GenAI System Architecture Overview.pdf](03_ai_ml_engineering/GenAI%20System%20Architecture%20Overview.pdf) | Source PDF (Pluralsight course) |
| [transformers_explained.md](03_ai_ml_engineering/transformers_explained.md) | Transformer architecture explained |

### MCP (Model Context Protocol)

| File | What it is |
|---|---|
| [mcp_knowledge_base/README.md](03_ai_ml_engineering/mcp_knowledge_base/README.md) | KB entry point |
| [01_mcp_foundations.md](03_ai_ml_engineering/mcp_knowledge_base/01_mcp_foundations.md) | What MCP servers are and how they run |
| [02_tool_call_decisioning.md](03_ai_ml_engineering/mcp_knowledge_base/02_tool_call_decisioning.md) | Tool routing patterns (rule-based, LLM-native, hybrid) |
| [03_contracts_by_stage.md](03_ai_ml_engineering/mcp_knowledge_base/03_contracts_by_stage.md) | Stage-by-stage interface contracts |
| [04_poc_map.md](03_ai_ml_engineering/mcp_knowledge_base/04_poc_map.md) | Map of POC projects in this repo |
| [05_agentic_orchestration_pattern.md](03_ai_ml_engineering/mcp_knowledge_base/05_agentic_orchestration_pattern.md) | Production agentic loop pattern (sanitised) |

### MCP POC Projects

| Project | What it does |
|---|---|
| [company_info_server/server.py](03_ai_ml_engineering/mcp_examples/company_info_server/server.py) | Minimal real MCP server with one tool |
| [minimal_mcp_company_info/](03_ai_ml_engineering/mcp_examples/minimal_mcp_company_info/README.md) | Production-lean MCP package with tests |
| [minimal_mcp_user_call_poc/app.py](03_ai_ml_engineering/mcp_examples/minimal_mcp_user_call_poc/app.py) | Host-side mock: LLM tool selection + confidence + validation |

### Agent Rating System

| File | What it is |
|---|---|
| [AGENT_RATING_INTERVIEW_PREP.md](03_ai_ml_engineering/agent_rating_system/AGENT_RATING_INTERVIEW_PREP.md) | Interview prep for agent rating concepts |
| [agent_rating_system.py](03_ai_ml_engineering/agent_rating_system/agent_rating_system.py) | Agent rating implementation |
| [demo_all.py](03_ai_ml_engineering/agent_rating_system/demo_all.py) | Full demo runner |

### Other

| File | What it is |
|---|---|
| [rag_example/rag_example.py](03_ai_ml_engineering/rag_example/rag_example.py) | RAG pipeline example |
| [skills_and_evals/accountresearchskill.md](03_ai_ml_engineering/skills_and_evals/accountresearchskill.md) | Account research skill spec |
| [skills_and_evals/Multi-Agent Enterprise Customer Service Orchestrator.md](03_ai_ml_engineering/skills_and_evals/Multi-Agent%20Enterprise%20Customer%20Service%20Orchestrator.md) | Multi-agent orchestration design |

---

## 04 — System Design

| File | What it is |
|---|---|
| [system_design_roadmap.md](04_system_design/system_design_roadmap.md) | System design study roadmap |
| [guid_generator.py](04_system_design/guid_generator.py) | GUID generator design |
| [rate_limiters/rate_limiter.py](04_system_design/rate_limiters/rate_limiter.py) | Basic rate limiter |
| [rate_limiters/SlidingWindowRateLimiter.py](04_system_design/rate_limiters/SlidingWindowRateLimiter.py) | Sliding window rate limiter |
| [rate_limiters/MultiResourceRateLimiter.py](04_system_design/rate_limiters/MultiResourceRateLimiter.py) | Multi-resource rate limiter |
| [file_transfer/file_tracker_1.py](04_system_design/file_transfer/file_tracker_1.py) | File transfer tracker v1 |
| [file_transfer/file_tracket_2.py](04_system_design/file_transfer/file_tracket_2.py) | File transfer tracker v2 |

---

## 05 — Behavioral

| File | What it is |
|---|---|
| [behavioral.md](05_behavioral/behavioral.md) | Behavioral question bank and STAR answers |
| [elevator_pitch.md](05_behavioral/elevator_pitch.md) | Personal elevator pitch |

---

## 06 — Study Plans

| File | What it is |
|---|---|
| [LEARNING_PATTERN_COACHING_PROFILE.md](06_study_plans/LEARNING_PATTERN_COACHING_PROFILE.md) | Your learning style profile and coaching approach |
| [interview_prep_plan.md](06_study_plans/interview_prep_plan.md) | General interview prep plan |
| [15_day_senior_ai_prep_plan.md](06_study_plans/15_day_senior_ai_prep_plan.md) | 15-day senior AI engineer prep plan |
| [staff_ai_engineer_prep_plan.md](06_study_plans/staff_ai_engineer_prep_plan.md) | Staff AI engineer prep plan |

**Company-specific prep:**

| File | Role / Company |
|---|---|
| [TERADATA_AGENTIC_AI_INTERVIEW_PREP.md](06_study_plans/company_specific/TERADATA_AGENTIC_AI_INTERVIEW_PREP.md) | Teradata — Agentic AI role |
| [ATLASSIAN_INTERVIEW_PREP.md](06_study_plans/company_specific/ATLASSIAN_INTERVIEW_PREP.md) | Atlassian — interview prep |
| [ATLASSIAN_PROBLEMS_SUMMARY.md](06_study_plans/company_specific/ATLASSIAN_PROBLEMS_SUMMARY.md) | Atlassian — problem summary |
| [VANGUARD_CHIEF_AI_ARCHITECT_INTERVIEW_PREP.md](06_study_plans/company_specific/VANGUARD_CHIEF_AI_ARCHITECT_INTERVIEW_PREP.md) | Vanguard — Chief AI Architect |
| [BANKING_INTERVIEW_GUIDE.md](06_study_plans/company_specific/BANKING_INTERVIEW_GUIDE.md) | Banking sector guide |
| [capital_one_gca_cram.md](06_study_plans/company_specific/capital_one_gca_cram.md) | Capital One GCA cram |

---

## Resumes

| File | |
|---|---|
| [Resume_AnkitaJain_teradata.pdf](resumes/Resume_AnkitaJain_teradata.pdf) | Resume — Teradata version |
| [Ankita_Jain_Resume_Motional.pdf](resumes/Ankita_Jain_Resume_Motional.pdf) | Resume — Motional version |

---

## Reference

| Resource | What it is |
|---|---|
| [reference/claude-cookbooks/README.md](reference/claude-cookbooks/README.md) | Anthropic Claude cookbook examples |

---

## Revision Mode — Where to Start

| Priority | File | Why |
|---|---|---|
| 1 | [GenAI_System_Architecture_Learning_Guide.md](03_ai_ml_engineering/GenAI_System_Architecture_Learning_Guide.md) | Most recent deep content — 5 modules from Pluralsight course |
| 2 | [dsa_warmup_templates.py](01_coding_dsa/dsa_warmup_templates.py) | Warm up before any coding round |
| 3 | [LEARNING_PATTERN_COACHING_PROFILE.md](06_study_plans/LEARNING_PATTERN_COACHING_PROFILE.md) | Remind yourself how you learn best |
| 4 | Company-specific prep doc for your next interview | Focus revision |
| 5 | [mcp_knowledge_base/](03_ai_ml_engineering/mcp_knowledge_base/README.md) | MCP concepts for agentic AI rounds |
