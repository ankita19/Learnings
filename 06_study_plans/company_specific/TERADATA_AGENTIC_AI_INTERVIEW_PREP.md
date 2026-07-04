# Teradata Principal Engineer Agentic AI Interview Prep

This guide is tailored to the Teradata Principal Engineer role focused on agentic AI, enterprise vector infrastructure, AI Studio, and production-grade observability and governance. It is also tuned to the current loop structure: two 45-minute interviews with a Staff Software Engineer and a Sr Staff Software Engineer.

## Interview Readout

- Company theme: enterprise AI that turns governed data into action.
- Role theme: principal-level ownership of agent frameworks, orchestration, evaluation, observability, and safe enterprise deployment.
- Likely bar: strong architecture judgment, technical depth on agents and LLM systems, and credible answers on governance, scale, and operational reliability.
- Likely interviewer lens:
  - Jeris Jawahar, Staff Software Engineer: implementation depth, APIs, orchestration choices, system design specifics, tradeoffs.
  - Mark Sandan, Sr Staff Software Engineer: platform strategy, production resilience, cross-team technical leadership, long-term architecture.

## End-To-End 3-Step Interview Plan

Assumption for planning: the 3 steps are recruiter or coordination screen, Jeris technical interview, and Mark architecture and leadership interview.

### Step 1: Recruiter or Introductory Screen

#### Goal

Show clean role fit, compensation and logistics alignment, and a crisp narrative for why Teradata and why this role.

#### What they are testing

- Why this role makes sense for your background now.
- Whether you understand the role is platform engineering for agentic AI, not generic model experimentation.
- Whether your compensation, timing, and work-style expectations are aligned.

#### Your answer shape

- 60-second background summary.
- Why Teradata: enterprise AI, governed data, production platforms, agentic systems.
- Why this role: platform primitives, observability, governance, developer enablement.
- What you want next: deep technical conversations about architecture and impact.

#### Prep checklist

- Finalize a 60-second intro and a 2-minute version.
- Prepare a clean answer for why you are exploring this move now.
- Be ready for compensation, notice period, interview availability, location, and work authorization questions.
- Have 2 thoughtful questions on team mission and interview process.

#### Strong message to land

I am not looking just to build isolated LLM features. I am most interested in building the reusable platform capabilities that let enterprise teams ship agentic AI safely, observably, and at scale.

### Step 2: Jeris Jawahar Technical Round

#### Goal

Demonstrate implementation depth on agent systems, APIs, memory, tool use, evaluation, and production failure handling.

#### What they are testing

- Can you design a concrete agent platform, not just talk conceptually?
- Can you reason about tool boundaries, state, retries, and correctness?
- Can you explain tradeoffs between single-agent, multi-agent, and deterministic orchestration?

#### Topics to prepare hard

- Agent loop design and termination logic.
- Memory taxonomy: session, task, knowledge, policy.
- Tool execution safety and identity propagation.
- Retrieval architecture and vector-store tradeoffs.
- Evaluation harnesses and debugging failed runs.
- API and SDK design for platform adoption.

#### Answer style for this round

- Use specific components, not abstractions alone.
- Name control points: gateway, orchestrator, tool registry, policy engine, trace store.
- Explain failure modes and recovery paths.
- Give concrete metrics: task success, tool accuracy, latency, override rate.

#### Likely question patterns

- Design an enterprise agent platform.
- How would you implement memory and context management?
- How would you evaluate and debug agent behavior?
- When would you use multi-agent versus a simpler workflow engine?
- How would you expose these capabilities as an SDK?

#### What to avoid

- Saying LangChain or AutoGen without explaining the surrounding platform.
- Treating vector DB choice as the main architecture decision.
- Speaking only at whiteboard level with no execution details.

### Step 3: Mark Sandan Architecture And Leadership Round

#### Goal

Show principal-level system judgment, platform strategy, governance maturity, and the ability to lead the technical roadmap across teams.

#### What they are testing

- Can you define what Teradata should build versus buy?
- Can you design for multi-team adoption, security, compliance, and long-term extensibility?
- Can you connect architecture choices to business outcomes and operating models?

#### Topics to prepare hard

- Platform roadmap for agent management, provisioning, orchestration, retirement, and governance.
- Multi-tenancy, isolation, entitlements, and zero-trust patterns for agents.
- Observability strategy tied to release gates and incident management.
- Drift detection, rollback, canarying, and post-release quality control.
- Operating model for platform teams versus product teams.
- Adoption strategy: standards without blocking experimentation.

#### Answer style for this round

- Start with principles and business outcomes.
- Then lay out architecture and tradeoffs.
- Close with adoption, measurement, and risk controls.
- Use org-level language: reusable platform, control plane, self-service, governance, SLOs, roadmap.

#### Likely question patterns

- What would the next-generation agent platform roadmap look like?
- How do you make agentic AI secure and governable by design?
- How do you prevent platform fragmentation across teams?
- How do you measure platform success after launch?
- What are the biggest risks in scaling multi-agent enterprise systems?

#### What to avoid

- Getting stuck in framework details instead of strategy.
- Sounding like a feature owner rather than a platform owner.
- Talking only about model capability instead of system reliability and adoption.

## Cross-Step Preparation Assets

Prepare these once and reuse them across all 3 steps:

1. A 60-second intro.
2. A 2-minute flagship project story.
3. Four STAR stories: platform adoption, technical conflict, AI quality or observability, production incident.
4. A 10-minute enterprise agent platform design answer.
5. A crisp build-versus-buy opinion.
6. A metrics set you can repeat naturally: quality, latency, cost, safety, adoption.

## Suggested Prep Sequence Before The Loop

### 5 to 7 days before

- Tighten intro, flagship story, and 4 STAR stories.
- Review Teradata business context and map your experience to agent platform ownership.
- Rehearse your enterprise agent platform design answer out loud.

### 3 to 4 days before

- Do one mock focused on Jeris-style technical depth.
- Drill memory, tool execution, evals, observability, and failure handling.
- Prepare 5 precise questions you may ask interviewers.

### 1 to 2 days before

- Do one mock focused on Mark-style architecture and principal leadership.
- Rehearse build-versus-buy, platform roadmap, governance, and adoption strategy.
- Review metrics, SLOs, and incident-response framing.

### Day of interview

- Review the 60-second intro, 4 stories, and your platform diagram.
- Skim your prepared questions for Jeris and Mark.
- Keep answers concise: 60 to 90 seconds by default, expand only when asked.

## Success Criteria By Step

- Step 1 success: they see a clean fit and move you forward confidently.
- Step 2 success: they believe you can build the platform correctly.
- Step 3 success: they believe you can shape the platform roadmap and raise engineering quality across teams.

## Your Experience To Role Mapping (Ankita-Specific)

Use this section as your anchor so you do not undersell your profile.

### Why your background is a strong fit

- You already operate at principal scope with 12 plus years across Microsoft and Bank of America.
- You have direct evidence of enterprise AI platform ownership, not only feature development.
- You have measurable outcomes in evaluation, governance, observability, and platform adoption.
- You have production experience with agentic systems, RAG assistants, MCP-powered tools, and CI/CD release gates.

### High-signal proof points to repeat

- Built offline and online LLM evaluation platforms integrated into release gates and adopted by 30 plus teams.
- Led Responsible AI guardrails and production observability with sustained SLOs of at least 95 percent groundedness and at least 90 percent usefulness.
- Shipped GA agentic AI systems and de-risked roadmap choices through 20 plus rapid POCs.
- Built RAG assistants and MCP-powered tools that reduced manual enterprise-data lookup by 75 percent.
- Led platform modernization and adoption at Bank of America across 25 internal lines with strong compliance posture.

### How to position your RAG concern

If asked about deep RAG internals, do not frame a gap. Use this framing:

My strongest skill is building production-grade AI and data platforms that make retrieval, evaluation, governance, and observability reliable at scale. I have shipped RAG assistants in enterprise settings and I focus on the engineering rigor that determines whether these systems succeed in production.

## Step-Wise Talk Track Using Your Background

### Step 1: Recruiter or Intro Screen

#### 60-second intro (custom)

I am a Principal AI and Data Platform Engineer at Microsoft with 12 plus years building distributed systems and enterprise AI platforms. I currently lead strategy and engineering for LLM evaluation and quality gates across D365 Sales AI, including offline and online evaluation platforms adopted by 30 plus teams. I also lead production Responsible AI controls and observability, sustaining strong groundedness and usefulness SLOs. Before Microsoft, I drove Spark platform modernization and adoption in regulated financial environments at Bank of America. I am excited about Teradata because this role combines exactly what I do best: building safe, scalable agent platforms with strong governance, developer usability, and measurable production outcomes.

#### What to emphasize

- Principal scope and cross-team influence.
- Platform ownership and measurable adoption.
- Production reliability and governance maturity.

### Step 2: Jeris Technical Round

#### What to lean on from your experience

- Evaluation platform architecture and CI/CD integration.
- Agentic systems shipped to GA.
- MCP-powered tool integration and retrieval workflows.
- Real production telemetry and error-budget management.

#### If asked system design, map to your shipped work

- Start with your evaluation and observability control plane experience.
- Add agent orchestration, memory tiers, and tool boundary controls.
- Close with concrete metrics from your Microsoft work.

#### Jeris round evidence snippets

- We moved from ad hoc quality checks to a standardized evaluation platform adopted by 30 plus teams.
- We added online production evaluation as a background scoring system to detect regressions without user-latency impact.
- We instrumented token cost, latency percentiles, and quality scores to support release decisions.

### Step 3: Mark Architecture and Leadership Round

#### What to lean on from your experience

- Principal-level roadmap and governance alignment.
- Platform architecture across multiple products and environments.
- Data governance, classification, sensitivity labeling, and enterprise controls.
- Prior experience in regulated systems and migration at scale.

#### Mark round evidence snippets

- Designed platform capabilities that scaled across multiple teams, not one product surface.
- Built governance and observability into the architecture rather than post-release patching.
- Drove cost and throughput improvements in data platforms while preserving reliability and compliance.

## STAR Stories (Customized)

Prepare these four stories in 2-minute and 4-minute versions.

1. LLM evaluation platform at Microsoft.
Situation: fragmented AI quality measurement and release risk.
Task: build a reusable quality control system across teams.
Action: designed offline and online eval platform, rubric scoring, side-by-side testing, CI/CD gates, live dashboards.
Result: adopted by 30 plus teams; regressions detected pre-release; improved release confidence.

2. Responsible AI and production observability.
Situation: customer-facing agents required safety, groundedness, and reliability.
Task: enforce policy and monitor production quality continuously.
Action: implemented guardrails, jailbreak defenses, telemetry across latency and cost, quality SLOs.
Result: sustained at least 95 percent groundedness and at least 90 percent usefulness.

3. Agentic assistants and tooling impact.
Situation: high manual lookup burden for enterprise teams.
Task: build usable assistants with trusted enterprise context.
Action: delivered RAG assistants and MCP-powered tools integrated into workflows.
Result: reduced manual data lookup time by 75 percent.

4. Bank of America platform modernization and adoption.
Situation: fragmented ETL and heavy manual reporting in regulated context.
Task: scale standardized data engineering practices across business lines.
Action: drove Spark framework adoption, lineage and data quality controls, migration from legacy stacks.
Result: adoption across 25 lines and major efficiency gains with compliance integrity.

## Personalized 7-Day Plan (Realistic)

### Day 1: Message Calibration

- Finalize 60-second intro and why-Teradata answer.
- Build one proof-point sheet with your top 10 measurable outcomes.
- Rehearse opening answers for Step 1 and Step 2.

### Day 2: Technical Design Drill

- Practice one 10-minute enterprise agent-platform design.
- Practice one 10-minute eval and observability design.
- Add specific tradeoffs: latency versus quality, autonomy versus control, cost versus reliability.

### Day 3: Jeris-Focused Mock

- Do one 45-minute technical mock with implementation depth.
- Drill memory design, tool execution boundaries, retry and fallback logic.
- Practice concise metric-backed explanations from your Microsoft work.

### Day 4: Mark-Focused Mock

- Do one 45-minute architecture and leadership mock.
- Practice roadmap framing, build versus buy, and platform operating model.
- Emphasize governance-by-design and cross-team adoption.

### Day 5: Behavioral and Influence Stories

- Polish the 4 STAR stories and add leadership conflict examples.
- Practice concise responses on mentoring, alignment, and difficult technical decisions.
- Tighten one story that shows principal-level org impact.

### Day 6: Pressure Rehearsal

- Run two back-to-back mocks: Jeris style then Mark style.
- Enforce timing: 60 to 90 second default answers, expand only if asked.
- Debrief weak spots and create final correction notes.

### Day 7: Interview-Day Playbook

- Light review only: intro, 4 stories, architecture diagram, metric sheet.
- Review interviewer-specific questions you will ask.
- Keep energy for the interviews; avoid heavy new material.

## Questions You Can Ask That Match Your Background

### Ask Jeris

- Which part of the agent platform is currently the biggest technical bottleneck: orchestration, evaluation, or tool execution?
- How does the team currently detect and triage quality regressions after deployment?

### Ask Mark

- What are the top architecture decisions this role must lead in the next two quarters?
- How do you balance platform standardization with product-team autonomy in agent development?

## Job Description Deconstruction (Staff Engineer - AI Platform)

Use this as your grounding layer so your answers mirror the posting language.

### What the role is explicitly about

- Building production-grade agent platforms, not isolated AI features.
- Designing agent frameworks, LLM pipelines, observability, and evaluation layers.
- Enabling secure-by-design autonomous agents with governance and accountability.
- Driving multi-agent orchestration, memory and context management, and enterprise adoption.
- Leading the technical roadmap for agent lifecycle: discovery, provisioning, orchestration, and retirement.

### What they will likely score hardest

- Systems depth in distributed, cloud-native, secure backend architecture.
- Practical handling of non-deterministic AI behavior in production.
- Ability to make AI measurable and debuggable with strong eval and observability discipline.
- Principal-level leadership across product, research, and platform teams.
- Developer platform thinking: APIs and SDKs that make safe adoption easy.

### Interview signal words to reuse naturally

- Control plane
- Secure-by-design
- Agent lifecycle management
- Observability and evaluation as release gates
- Guardrails and policy enforcement
- Multi-tenant safety and accountability
- Developer enablement through SDK and APIs
- Production reliability, drift detection, and closed-loop improvement

## Your JD Match Matrix (Tailored To Your Resume)

### 1. Agent frameworks and intelligent agents at scale

JD asks for: design and deployment of secure, autonomous agents.
Your evidence: shipped multiple GA agentic systems at Microsoft using Copilot Studio and Agent Builder; built MCP-powered tools and RAG assistants; de-risked direction through 20 plus POCs.

### 2. Evaluation and observability platform ownership

JD asks for: measurable, debuggable, trustworthy production AI.
Your evidence: built offline and online evaluation platforms with CI/CD release integration adopted by 30 plus teams; implemented production telemetry and quality dashboards.

### 3. Governance, policy, access control, and safety

JD asks for: secure-by-design agents with visibility and accountability.
Your evidence: implemented Responsible AI guardrails, policy enforcement, jailbreak defenses, and groundedness controls; built governance-heavy Purview features including classification and sensitivity labeling.

### 4. Distributed systems and cloud-native architecture

JD asks for: scalable infrastructure and backend architecture.
Your evidence: long history across Azure microservices, Spark pipelines, Cosmos DB, Kubernetes, and high-throughput data platforms in regulated environments.

### 5. Cross-functional principal leadership

JD asks for: lead roadmap and collaborate across org boundaries.
Your evidence: principal advisor role, team leadership across evaluation and platform engineering, adoption across 30 plus teams at Microsoft and 25 business lines at Bank of America.

### 6. CI/CD, reliability, and production operations

JD asks for: testing, observability, and production rigor.
Your evidence: CI/CD quality gates, online evaluation in production, SLO ownership, alerting systems, and proactive reliability controls.

## Potential Gaps And Strong Mitigation Framing

### Gap 1: Very deep framework-name trivia

If pressed on a specific framework detail, redirect to architecture principles and shipped outcomes: orchestration boundaries, tool permissions, evaluation gates, and observability.

### Gap 2: Deep RL or cognitive architecture depth

Treat this as desirable, not core. Bridge from your production agent and evaluation systems and explain where RL-style policy learning could fit later.

### Gap 3: Open-source contribution signal

If you do not have major OSS contributions, emphasize internal platform leverage at enterprise scale, reusable abstractions, and measurable adoption.

## 7-Day Plan Aligned 1:1 To This JD

### Day 1: JD Message Map and Intro Alignment

- Convert JD into 6 themes: agent platform, security, observability, eval, developer APIs, leadership.
- Rehearse 60-second and 2-minute intros using JD wording.
- Build one page: JD requirement to your proof points.

### Day 2: Agent Platform Design For Step 2

- Practice one canonical design: secure enterprise agent control plane.
- Include lifecycle: discovery, provisioning, orchestration, retirement.
- Include memory/context strategy and tool governance.

### Day 3: Measurability, Evals, And Debuggability

- Practice answering how to make AI measurable and debuggable.
- Prepare exact metrics and SLO examples from your Microsoft work.
- Rehearse online eval plus release-gate story until crisp.

### Day 4: Security, Governance, And Multi-Tenant Safety

- Drill identity propagation, access control, policy checks, and audit traces.
- Practice secure-by-design answer pattern: prevent, detect, contain, recover.
- Prepare one incident-style story on safeguards and mitigations.

### Day 5: Developer Platform And Adoption Narrative

- Practice how you would expose agent capability through SDK and APIs.
- Cover platform standards versus team flexibility.
- Rehearse adoption strategy and anti-fragmentation operating model.

### Day 6: Two Interview Simulations

- Mock 1 (Jeris style): deep technical implementation, component details, failure handling.
- Mock 2 (Mark style): roadmap, build-versus-buy, operating model, risk and governance.
- Debrief and cut answers down to 60 to 90 second defaults.

### Day 7: Final Execution Day

- Light review only: intro, 4 STAR stories, architecture diagram, metric sheet.
- Review 5 interviewer questions and closing statements.
- Enter interviews with principle-first, metric-backed, concise delivery.

## Interview-Day Rapid Checklist (10 Minutes)

- One sentence role fit: principal platform engineer for safe agentic AI.
- One architecture headline: model is not the control plane.
- One quality headline: eval and observability are release gates.
- One safety headline: secure-by-design with policy-enforced tool use.
- One adoption headline: SDK and platform standards that teams can actually use.

## Core Positioning

- Position the agent platform as a control plane, not a prompt wrapper.
- Treat AI agents as bounded workers operating under orchestration, policy, and observability.
- Keep deterministic systems in charge of critical decisions, access control, and side effects.
- Show that memory, retrieval, planning, and tool use are engineering problems first and prompting problems second.
- Connect every technical choice to enterprise outcomes: trust, latency, cost, governance, developer adoption, and measurable business value.

## 90-Second Introduction

My background sits at the intersection of data platforms, AI engineering, and production governance. The work most relevant here is building reusable LLM and agent infrastructure rather than one-off demos: orchestration layers, RAG pipelines, evaluation frameworks, and observability patterns that multiple teams can adopt safely.

What makes this Teradata role especially interesting is that the problem is not just model integration. It is building the platform primitives that make agents usable in enterprise settings: controlled tool execution, memory and context management, policy enforcement, drift monitoring, release gating, and developer-friendly abstractions. That is the kind of systems problem I like most because it requires architecture rigor, operational discipline, and clear tradeoffs between flexibility and control.

## What Teradata Is Likely Testing

### 1. Agent architecture depth

- Can you explain planning loops, tool use, handoffs, memory, and failure handling beyond buzzwords?
- Can you distinguish where to use single-agent, orchestrated multi-agent, and deterministic workflow engines?
- Can you explain how to prevent agents from becoming opaque and ungovernable?

### 2. Production AI engineering

- Can you define SLOs for latency, groundedness, task success, and cost?
- Can you explain evals, canary rollout, regression detection, and incident response?
- Can you make agent systems debuggable with traces, state snapshots, and audit logs?

### 3. Enterprise platform thinking

- Can you build platform capabilities other teams adopt through APIs and SDKs?
- Can you separate core control points to own from commodity layers to source?
- Can you design for multi-tenancy, identity, entitlements, and policy isolation?

### 4. Principal-level leadership

- Can you define a technical roadmap, not just a component?
- Can you influence product, research, and platform teams with a strong opinionated architecture?
- Can you translate deep technical tradeoffs into business language?

## Strong Architecture Opinion

For enterprise agentic AI, I would build a layered platform:

1. An agent gateway for identity, request classification, rate limiting, tenant isolation, and policy bootstrap.
2. An orchestration layer that manages state, workflow routing, planning loops, tool permissions, retries, fallbacks, and human handoff.
3. A retrieval and memory layer split into short-term session state, durable task history, and governed enterprise knowledge.
4. A tool execution layer that exposes enterprise capabilities through typed APIs with scoped credentials and policy checks.
5. An evaluation and observability layer that captures traces, state transitions, tool outcomes, groundedness, latency, cost, and policy violations.
6. A model abstraction layer that preserves optionality across model providers and task-specific models.

The key principle is that the model is not the control plane. The orchestrator, policy engine, identity boundary, and telemetry stack are the real platform assets.

## Likely Questions And Tight Answer Direction

### 1. How would you architect an enterprise agent platform?

Lead with layers: gateway, orchestration, memory, tooling, evals, observability. Emphasize that agents propose actions while the platform enforces identity, policy, and execution boundaries. Close with why this matters: platform reuse, safe adoption, and operability.

### 2. When do you use multi-agent systems versus a single orchestrated agent?

Use a single agent for narrow, linear tasks where coordination overhead is not justified. Use multi-agent systems when you have natural role decomposition, heterogeneous tools, or parallelizable subtasks, but keep a central orchestrator so agents do not directly compete for shared state or side-effecting actions.

### 3. How would you handle memory and context management?

Separate memory by purpose:

- Session memory for short-lived conversational state.
- Task memory for workflow progress and intermediate artifacts.
- Knowledge memory for governed enterprise facts retrieved through RAG.
- Policy memory for identity, entitlements, and operational constraints.

Never let memory become an unbounded prompt dump. Use freshness rules, compaction, provenance, and clear retention policies.

### 4. How do you make agents safe in enterprise environments?

Use least privilege, scoped tools, explicit action classes, approval gates, and full traceability. High-risk actions should require deterministic validation or human approval. Treat prompt injection, tool misuse, and data exfiltration as platform threats, not just model issues.

### 5. What would observability look like for AI agents?

Capture end-to-end traces for request, planning steps, retrieval results, tool calls, policy decisions, and outputs. Track latency, token cost, groundedness, task completion, tool failure rate, override rate, and policy-violation attempts. Observability should support three use cases: debugging, governance, and release decisions.

### 6. How would you evaluate agent quality?

Use layered evals:

- Offline benchmark sets for task success, faithfulness, and tool selection.
- Workflow simulation for multi-step completion and recovery behavior.
- Shadow and canary evaluation in production.
- Human review for ambiguity, usefulness, and trust.

Do not evaluate only final text. Evaluate intermediate decisions, tool choice, state transitions, and whether the system knew when to stop or escalate.

### 7. How would you detect drift in an agent platform?

Track input drift, retrieval drift, tool-usage drift, output-quality drift, and business-outcome drift. A stable text style with worsening tool selection is still a production issue. Define severity thresholds tied to workflow criticality and connect them to rollback or tighter human review.

### 8. How do you prevent agent sprawl across the enterprise?

Provide a common SDK, policy model, tool registry, evaluation harness, and deployment path. Make the safe path the easiest path. If teams can only move fast by building outside the platform, the platform is failing.

### 9. How do you expose agentic capabilities to developers?

Through typed APIs and SDKs with built-in tracing, auth, retry semantics, policy hooks, and evaluation support. Product teams should declare workflow intent, tools, and risk tier rather than hand-rolling orchestration from scratch.

### 10. How do you choose between building and buying?

Buy fast-moving commodity layers like model access or basic vector infrastructure if they remain swappable. Build the control points: orchestration, governance, evaluation, developer abstractions, and deep enterprise integration.

## Questions You Should Expect To Push Hard On

### Agent loops

- How do you bound planning depth?
- When do you terminate versus retry?
- How do you recover from bad tool outputs?
- How do you avoid infinite self-reflection loops?

### Memory and vector systems

- When do you store information in vector search versus structured state?
- How do you handle stale or conflicting memory?
- How do you keep retrieval grounded across tenants or business units?

### Security and governance

- How do you apply zero-trust ideas to agents?
- How do you propagate user identity into agent tool calls?
- How do you audit downstream actions taken on behalf of a user?

### Platform adoption

- How do you get multiple teams to use your agent framework?
- What do you standardize versus leave flexible?
- How do you keep the platform from blocking experimentation?

## Good Technical Opinions To Use

- Agent frameworks should encode control flow, permissions, and telemetry. Prompts alone are not architecture.
- Most enterprise agent failures come from state, tool, and policy design, not model IQ.
- Multi-agent systems are easy to demo and hard to operate. Use them only when role separation produces clear value.
- Vector search is not memory by itself. Memory needs lifecycle, provenance, and retrieval discipline.
- Evals must be release gates, not dashboard decorations.
- If humans cannot reconstruct why an agent acted, the system is not production-ready.

## Metrics To Mention

- Task success rate
- Groundedness or citation coverage
- Tool selection accuracy
- Multi-step completion rate
- Human override rate
- Escalation rate
- Latency per workflow stage
- Cost per successful task
- Policy violation block rate
- Time to debug or reproduce failed runs

## High-Value Stories To Prepare

Prepare 4 stories and keep each to 2 minutes:

1. A platform or framework you built that multiple teams adopted.
2. A time you improved evaluation, observability, or release quality for AI systems.
3. A technical disagreement where you changed architecture direction through reasoning and data.
4. A production incident or failure mode that changed how you designed safeguards.

For each story, make sure you can answer:

- What scaled beyond your immediate team?
- What hard tradeoff did you make?
- What metric improved?
- What would you do differently now?

## Questions To Ask Jeris Jawahar

- Where does the team currently feel the most friction: orchestration, evals, tool integration, or governance?
- How opinionated is the internal agent platform today versus a collection of libraries and patterns?
- What makes an engineer successful in the first six months on this team?

## Questions To Ask Mark Sandan

- What architectural decisions over the next year will most shape Teradata's agent platform strategy?
- Where do you want stronger platform standardization versus team-level flexibility?
- What failure modes or scaling limits are you most concerned about as agent adoption expands?

## 5-Day Prep Plan

### Day 1

- Tighten your 90-second introduction.
- Prepare 4 stories using STAR with principal-level scope.
- Review orchestration, memory, tool execution, and eval terminology until the wording feels natural.

### Day 2

- Practice designing an enterprise agent platform out loud in 10 minutes.
- Rehearse multi-agent versus single-agent tradeoffs.
- Prepare one crisp answer on build versus buy.

### Day 3

- Review observability, drift, and incident response patterns for AI systems.
- Practice explaining policy enforcement, identity propagation, and safe tool execution.

### Day 4

- Run a mock focused on principal-level behavioral questions.
- Tighten examples showing org-wide influence, not just feature delivery.

### Day 5

- Do one final mock with concise 60 to 90 second answers.
- Prepare closing questions for each interviewer.
- Review key metrics and architecture principles.

## Red Flags To Avoid

- Talking about agents as autonomous magic instead of controlled systems.
- Treating RAG or vector DBs as a complete architecture answer.
- Giving only model-centric answers without APIs, state, tool design, or observability.
- Describing team-level implementation details without principal-level platform thinking.
- Saying safety is a post-processing filter instead of an end-to-end system property.

## Final Reminder

For Teradata, the strongest signal is that you can build the platform that makes agentic AI reliable at enterprise scale. Keep returning to control planes, policy-aware execution, developer enablement, observability, and measurable production quality.