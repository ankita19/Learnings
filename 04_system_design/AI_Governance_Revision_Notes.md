# AI Governance — Revision Notes
*Source: "Strategies for Effective AI Governance" (Doru Catana)*

---

## 1. What is AI Governance?

> Framework of **policies, procedures, and roles** that manage AI risk throughout the system lifecycle.

**Why not just use existing IT governance?** AI is different because it:
- Learns from data → behavior changes over time
- Makes hard-to-explain decisions
- Can create feedback loops that amplify bias

**Core components of proper AI governance:**
- Governance committee with clear decision rights
- Documented policies for development & deployment
- AI-specific risk assessment protocols
- Testing procedures to validate outputs
- Monitoring for drift/performance issues
- Incident response plans

**Cautionary example:** Credit scoring AI deployed without governance → undervalued properties in minority neighborhoods → fair lending compliance issue discovered 6 months later. Basic bias testing + monitoring would have caught it early.

---

## 2. Stakeholders & Their Deliverables

| Stakeholder | Responsibility | Deliverable |
|---|---|---|
| **Executives/Board** | Approve framework, set risk appetite, allocate resources | Formal AI governance charter (roles + reporting lines) |
| **AI Developers/Data Scientists** | Document design decisions, data sources, testing | Model card per AI system |
| **Risk & Compliance** | Adapt existing frameworks to AI-specific risks | AI risk register (classifies systems by impact) |
| **Business Units (deploying AI)** | Understand customer/ops impact | Impact assessment document |

**Key tip:** Don't over-engineer — start with high-impact systems, then expand.

---

## 3. Four Essential Principles

1. **Transparency**
   - Data provenance tracking
   - Feature importance analysis
   - Explainability mechanisms
   - Clear user communication about AI involvement

2. **Accountability**
   - Documented sign-off before deployment
   - Clear ownership of monitoring
   - Defined escalation paths
   - Recorded governance committee reviews

3. **Fairness**
   - Demographic impact testing pre-deployment
   - Regular bias audits
   - Segmented performance metrics (protected characteristics)
   - Documented, use-case-specific fairness definitions

4. **Practical first step:** Build a simple inventory of current AI systems (many orgs don't know what they're using) → rate by impact/risk → prioritize.

---

## 4. NIST AI Risk Management Framework (RMF)

*Not legally binding, but the de facto industry standard. Four continuous functions:*

| Function | What It Means | Example Action |
|---|---|---|
| **GOVERN** | Build org structure | Governance committee charters, AI policies, escalation lines |
| **MAP** | Identify context & impact | Document system boundaries, data flows, affected stakeholders |
| **MEASURE** | Analyze & track risk | Metrics, adversarial testing, monitoring dashboards, thresholds |
| **MANAGE** | Address identified risks | Prioritize by likelihood/impact, controls, feedback loops |

**Real example (healthcare org):** 3-tier structure — executive AI committee (quarterly), technical review board (monthly), embedded AI risk officers per business unit.

**Measure function example (recommendation system):** Track recommendation diversity, content quality, user satisfaction, demographic impact → dashboard with red/yellow/green thresholds → triggers retraining or human review.

---

## 5. Regulatory Landscape (Quick Reference)

| Region/Body | Focus |
|---|---|
| **EU AI Act** | Classifies AI systems by risk level |
| **US (no federal law)** | FTC (unfair/deceptive practices), EEOC (hiring discrimination), CFPB |
| **Canada** | AI Data Act — impact assessments for high-impact systems |
| **China** | Regulations targeting recommendation algorithms |

**Industry-specific:**
- **Financial services** → fair lending laws + Model Risk Management (OCC, Fed, FDIC expect governance beyond NIST)
- **Healthcare** → HIPAA + FDA framework for AI as medical devices
- **Hiring/Employment** → EEOC watching disparate impact
- **Retail/Consumer** → FTC wants clear AI-disclosure to consumers

**Practical takeaway:** Align with NIST first → layer industry-specific controls on top. **Document everything** ("if it's not documented, it didn't happen").

---

## 6. Implementation Blueprint

### A. Risk Assessment (simple 2-axis model)
- Score **Probability** (1–5) × **Impact** (1–5) per AI system
- High-high scores = immediate governance priority
- One-page template — 5 questions:
  1. What decisions does this AI influence?
  2. Who could be harmed if it fails?
  3. What's the worst realistic outcome?
  4. What controls exist to prevent this?
  5. How would we know if it's happening?

### B. Governance Structure (3 components)
1. **AI Governance Committee** — lean (5–7 people), technical + legal + business reps. Approves high-risk deployments, reviews incidents, updates policy.
2. **Dedicated AI oversight role(s)** — bridge between technical teams and leadership.
3. **Clear escalation paths** — e.g., traffic-light system (Green = routine, Yellow = within a week, Red = immediate).

**Bank example:** AI review board (biweekly), CDO as governance lead, traffic-light escalation.

### C. Documentation Requirements (minimum viable)
- AI inventory (purpose, data sources, risk rating)
- Governance charter (roles, decision rights)
- Risk assessments (per system)
- Testing records (pre-deployment evaluation proof)
- Incident logs

---

## 7. 8-Week Rollout Roadmap

| Week(s) | Action |
|---|---|
| 1 | Build AI inventory (survey departments, include vendor/3rd-party AI tools) |
| 2–3 | Initial risk assessments on high-impact systems; document gaps |
| 4 | Stand up governance structure (roles, recurring meetings) |
| 5–6 | Minimum viable documentation (templates, highest-risk systems first) |
| 7–8 | Begin monitoring (select metrics, set thresholds) |

---

## 8. Common Challenges → Solutions

| Challenge | Solution |
|---|---|
| Don't know where all AI systems are | Email survey to dept heads + check procurement for vendor tools |
| Technical teams resist as "bureaucracy" | Involve them in process design; keep docs lightweight |
| No in-house AI expertise | Cross-functional team + lean on NIST + outside expertise for setup |
| Leadership doesn't prioritize it | Frame as risk management/competitive advantage; cite recent AI failures |
| Overwhelmed by scope | Start with highest-risk systems only, expand gradually |

**Closing principle:** *"Perfect is the enemy of good."* Start small, focus on high-impact areas, build from there.

---

## Quick-Recall Summary (for last-minute review)

- **Definition:** AI governance = policies + procedures + roles managing AI risk across the lifecycle
- **4 principles:** Transparency, Accountability, Fairness, (+ practical inventory-first mindset)
- **NIST RMF functions:** Govern → Map → Measure → Manage
- **3 governance structure components:** Committee, oversight role, escalation path
- **5 documentation musts:** Inventory, Charter, Risk assessments, Testing records, Incident logs
- **Golden rule:** Start with highest-impact/highest-risk systems, document everything, expand gradually
