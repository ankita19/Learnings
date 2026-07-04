# Behavioral Stories — "POCs I Killed"

Two defensible, drill-down-proof stories for Staff/Senior AI interviews.
Both use the D365 Sales AI context. **Plug in real numbers and tool names** where estimated.

Core trait they demonstrate: *I measure honestly and kill what doesn't earn its cost.*

---

## Story 2 — Killed the fully-autonomous lead qualification agent

**Signal:** risk judgment + Responsible AI (the regulated/finance signal).

### High-level summary
We built a Sales Qualification agent in D365 Sales. The tempting version qualified
leads *fully autonomously* — writing the decision straight back to CRM. Eval showed an
unacceptable **false-disqualify rate**, so I killed the autonomous write-back and shipped
a **human-in-the-loop** version: the agent drafts, the seller approves.

### Situation & stakes
Sellers in D365 Sales are flooded with inbound leads and spend hours triaging them manually,
which means good leads go cold while they work low-value ones. The pitch was an agent that
auto-qualifies leads against **BANT** (Budget, Authority, Need, Timeline) so sellers focus
only on the best. The catch: in a sales/revenue context, a wrong **auto-disqualify** silently
discards a real opportunity — there's no error message, the lead just disappears. So the bar
for acting autonomously is high, and the cost of being wrong is asymmetric (a false-qualify
wastes a little seller time; a false-disqualify loses revenue and nobody notices).

### The use case, step by step
1. **Trigger:** A new lead lands in D365 Sales. The goal was to auto-assess BANT and
   prioritize so sellers work the best leads first.
2. **Context gathering (tools):** The agent calls tools to pull the Lead, related
   Account/Contact, and Activity history (emails, meetings) from **Dataverse**, plus
   firmographic enrichment.
3. **Reasoning:** An orchestrated LLM step assesses each BANT dimension against the gathered
   evidence and produces a **structured output** — a per-dimension assessment, an overall
   **qualification score**, a **written rationale**, and a **recommended action**
   (qualify / disqualify / route). The prompt instructed it to ground every claim in the
   record data.
4. **The autonomous part (what we tested):** A write-back tool that *automatically* set the
   lead status and created or closed the opportunity in CRM — no human in the path.
5. **Guardrails:** Responsible AI checks (grounding, policy) on the output before any action.

### How I evaluated it
- Built an eval set of **historical leads with known outcomes** (what the seller actually
  decided / which converted) — ground truth.
- Measured three things, not just aggregate accuracy:
  - **Groundedness** — did the rationale cite real record data, or invent it?
  - **Accuracy vs. seller decision.**
  - **False-disqualify rate** — the failure mode that actually costs money.
- Used an LLM-as-judge for rationale quality, plus direct comparison to ground-truth outcomes.

### Why I killed it
Aggregate accuracy looked fine, but the **false-disqualify rate was too high** — the agent
would *confidently* disqualify genuinely good leads, sometimes hallucinating "no authority"
or missing a buying signal. In a revenue context, a confident wrong "disqualify" silently
kills a real opportunity — the cost is asymmetric and invisible. Groundedness also dipped
below our bar on edge cases.

### Why the agent qualified leads wrong (root cause — for drill-down)
Pick 2–3 of these to speak to. #1 is the strongest and most defensible.

1. **Data sparsity → it treated "missing" as "negative" (the big one).** Early-stage leads
   have thin records — Budget blank, no title on the contact, two activities total. The
   agent read an empty Authority field and concluded "no authority → disqualify," when a
   human knows **absence of evidence isn't evidence of absence**. Single largest driver of
   false disqualifies.
2. **It hallucinated / over-inferred to fill the gaps.** With thin data, instead of saying
   "not enough info," it inferred from weak proxies and invented a rationale that *sounded*
   grounded ("limited budget authority") but wasn't supported by any field. That's why
   groundedness dipped.
3. **BANT requires context that isn't in the structured data.** "Need" and "Authority" are
   judgment calls — sellers use industry patterns, who really signs in that org, how the
   account behaved before. None of that lives in Dataverse fields, so the model scored with
   **less context than the seller has**, and confidently.
4. **Free-text signal extraction was error-prone.** A lot of intent lives in email/meeting
   notes — multi-stakeholder threads, hedged language, sarcasm. The model misread sentiment
   and intent in those.
5. **No calibration — confident even when it shouldn't be.** High-confidence scores on
   low-evidence leads, with no uncertainty signal, so I couldn't even safely auto-act on
   just the confident cases and route the rest. Confidence didn't track correctness.
6. **Aggregate accuracy hid it (class imbalance).** Most inbound leads genuinely are low
   quality, so aggressive disqualifying *looks* accurate on average while failing on the
   **rare high-value leads that matter**. That's why I measured false-disqualify rate
   separately.

**Tight one-sentence version:**
> "The core failure was data sparsity — early leads have incomplete records, and the model
> treated missing fields as negative signals and disqualified, often inventing a confident
> rationale to justify it. The judgment that fills those gaps lives in the seller's head,
> not in CRM fields." — which is exactly why human-in-the-loop was the right fix.

### What I shipped instead
Reframed as **human-in-the-loop**: the agent drafts the qualification, score, and reasoning
into the seller's view; the seller approves or edits in one click. Kept ~80% of the value
(speed, consistency, no blank-page problem) and removed the catastrophic failure mode. The
seller's edits also became a **feedback signal** — labeled data I could use to improve the
model toward earning more autonomy later.

### Results / outcome
- Removed the false-disqualify risk entirely (no silent revenue loss).
- Still cut seller triage time meaningfully because the draft + rationale does the heavy lifting.
- Turned every seller correction into training/eval signal — a path to autonomy, not a dead end.
*(Plug in your real numbers: % triage-time saved, adoption, accuracy of the assist.)*

### "Why not just fix the model instead of falling back to a human?" (have this ready)
> "You can — and that was the roadmap, not the ceiling. The fixes are real: prompt the model
> to output 'insufficient evidence' instead of guessing, add **confidence calibration** so we
> only auto-act on high-confidence cases and route the rest, and **enrich sparse records**
> before scoring. But those take time to build and prove. Human-in-the-loop let us ship value
> *safely today* while collecting the labeled data to earn autonomy. It was a staged risk
> decision: act autonomously only once the agent clears the bar, on the slice where it's
> trustworthy — not a binary 'autonomous or nothing.'"

### One-line lesson
> "A great demo isn't a production bar. I measure the failure mode that actually hurts —
> here, false disqualifies — not just average accuracy. And where a confident wrong answer
> is expensive, I keep a human in the loop until the agent earns the trust to act alone."

### Anticipated follow-ups (with answers)

**"How did you define ground truth?"**
> Historical leads with known outcomes — the seller's actual qualify/disqualify decision and
> whether the lead converted. I treated converted-but-the-agent-would've-disqualified as the
> critical error class. I also acknowledged label noise (seller decisions are subjective) and
> didn't over-trust a single source.

**"Why trust false-disqualify rate over overall accuracy?"**
> Class imbalance — most inbound leads really are low quality, so an aggressive disqualifier
> looks accurate on average while failing on the rare high-value leads that matter. The
> headline number hid the failure; the segmented metric exposed it.

**"What bar would the agent have needed to act autonomously?"**
> A low, bounded false-disqualify rate on a *calibrated, high-confidence* slice — i.e. let it
> auto-act only where it's confident and demonstrably right, and route everything else to a
> human. Autonomy on a slice, not all-or-nothing.

**"How is the human-in-the-loop version actually better, not just safer?"**
> It removes the catastrophic failure mode, keeps most of the time savings, *and* generates
> labeled corrections that feed back into improving the model — so it's both safer and a
> faster path to eventual autonomy.

**"Couldn't better prompting / a bigger model have fixed it?"**
> Partly — see the "why not just fix the model" answer above. But the core gap was *missing
> context* (judgment that lives in the seller's head, not in CRM fields). No prompt conjures
> data that isn't there; the right move was to either enrich the data or keep the human who
> has that context.

---

## Story 3 — Killed the livesite DRI assistant that hallucinated on bad TSGs

**Signal:** knowledge-base / data-quality discipline + abstention design + high-stakes
reliability — *"garbage in, garbage out"*: a RAG assistant can't outrun a weak knowledge
base, and an honest "I don't know" beats a confident wrong answer.

### High-level summary
We built an internal assistant to help on-call DRIs during livesite incidents — paste a
symptom, get suggested mitigation steps. In eval it gave **confident but wrong** guidance,
because our underlying **TSGs (troubleshooting guides) were sparse, stale, and
inconsistent**. A wrong answer mid-incident is worse than no answer, so I killed the
auto-answer version and **pivoted the tool from asserting conclusions to generating the
investigation query** the DRI runs — answer comes from real telemetry, human stays in the
loop — plus fixing the knowledge base with an abstain-first design.

### Situation & stakes
On-call DRIs get paged during livesite incidents and have to diagnose and mitigate fast,
often digging through scattered TSGs and past incidents under pressure. The pitch: an
assistant that takes the symptom/alert and instantly suggests the right mitigation. But in a
live incident the cost of a wrong answer is severe — a confident-but-wrong mitigation can
**prolong the outage, send the DRI down the wrong path, or make it worse**. And trust is
brittle: one confident wrong answer during a Sev2 and DRIs abandon the tool for good.

### The use case, step by step
1. **Trigger:** DRI gets paged, pastes the alert/symptom (or links the ICM incident) into the assistant.
2. **Retrieval:** The assistant searches the knowledge corpus — TSGs, runbooks, wiki, past
   resolved incidents — for relevant troubleshooting content.
3. **Generation:** The LLM synthesizes a suggested diagnosis + mitigation steps, grounded in
   the retrieved docs.
4. **(Intended) action:** The DRI follows the steps to mitigate faster.

### How I evaluated it
- Built an eval set from **real past incidents with known root causes / correct mitigations**
  (ground truth from resolved ICMs).
- Measured **groundedness** (are the steps actually supported by a real TSG?), **correctness**
  vs the known mitigation, and **hallucination rate** (invented steps/commands).
- Crucially, measured behavior on incidents with **no good TSG** — did it abstain, or
  confidently invent an answer?

### Why I killed it / root cause
The failure wasn't the model — it was the **knowledge base**. Root causes:
1. **Sparse / incomplete TSG coverage** — many incident types simply had no good guide, so
   there was nothing correct to retrieve.
2. **Stale & inconsistent content** — old TSGs with deprecated steps; the model surfaced
   outdated mitigations as if current.
3. **The model answered anyway instead of abstaining** — when retrieval returned weak or
   irrelevant chunks, it filled the gap with plausible-but-wrong steps (hallucinated
   commands / config).
4. **No "I don't know" path** — low-relevance retrieval still produced a confident answer.

Net: **confident, wrong mitigation guidance** — exactly the failure mode you can't ship into
a live incident.

### What I shipped / did instead
Killed the confident auto-answer. Refocused on:
- **Abstain-first design:** if retrieval relevance/confidence is below threshold, the tool
  says *"no reliable TSG for this"* and links what it did find — no generated mitigation.
- **Retrieval-only / source-surfacing mode:** point DRIs to the actual TSG / past-incident
  links instead of synthesizing steps, so a human verifies before acting.
- **Turned the gap analysis into a content roadmap:** the eval exposed exactly which
  high-frequency incident types lacked TSGs — which drove authoring/refresh of those first.
- (Optional) Re-scoped any generation to **only the areas with strong, current TSG coverage**.

### How it evolved — the version that actually worked (human-in-the-loop)
The key pivot: I moved the tool **from asserting conclusions to generating the investigation
query.** Instead of telling the DRI *"the problem is X, do Y"* (which it couldn't do reliably
without good TSGs), the redesigned tool takes the symptom and **generates the diagnostic
query** — the Kusto/log query (or the query against the lead/org data) the DRI should run to
pull ground truth. The DRI runs it, sees **real telemetry**, and makes the call.

Why this works where the first version failed:
- The **answer now comes from real data, not the model's memory** — so there's nothing to
  hallucinate. The model's job shrank to "write the right query," which is far more reliable
  than "diagnose the incident."
- The **human stays in the loop** as the interpreter — the DRI validates the query and reads
  the actual results, exactly like the human-in-the-loop fix in Story 2.
- It still delivers the real value (speed — getting to the right data fast under pressure)
  without the catastrophic failure mode of a confident wrong mitigation.

### Results / outcome
- Eliminated the dangerous failure mode — no confident wrong mitigations in incidents.
- Produced a **prioritized TSG-gap list** that made the knowledge base measurably better —
  the actual prerequisite for the assistant to ever work.
- Preserved DRI trust by being honest about uncertainty.
*(Plug in real numbers: hallucination rate before/after, % incidents with TSG coverage, adoption.)*

### One-line lesson
> "A RAG assistant is only as good as the knowledge it retrieves from — garbage in, garbage
> out. The bottleneck wasn't the model, it was the TSGs. And in a high-stakes path like
> livesite, an honest 'I don't have a reliable answer' beats a confident wrong one every
> time. So I fixed the knowledge base instead of shipping a confident hallucination."

### Anticipated follow-ups (with answers)

**"Couldn't a better model or more prompting fix the hallucination?"**
> No — the gap was missing/poor source content. No model invents a *correct* mitigation that
> was never documented. The fix is content + abstention, not a bigger model.

**"How did you detect hallucination?"**
> Compared the generated steps against the retrieved sources (groundedness check) and against
> the known resolutions from past ICMs; flagged any step with no supporting source.

**"How do you make it abstain reliably?"**
> Threshold on retrieval relevance/confidence — if below the bar, refuse to generate and
> surface sources only. Tune the threshold on the eval set to trade off coverage vs. risk.

**"Wasn't killing it a failure?"**
> The opposite — shipping a confident-wrong livesite tool would've been the failure. Killing
> the auto-answer protected DRI trust and redirected effort to the real bottleneck (the TSGs),
> which is the durable fix that makes the assistant viable later.

---

## Delivery shape (use for either story, ~45 sec)
1. **The tempting idea** ("the exciting version was…")
2. **What you built + how you tested it** (the POC + the eval)
3. **What the data showed** (the honest result that killed it)
4. **The decision + what you shipped instead**
5. **The one-line lesson** (the reusable principle)

## Why this pairing works
- **Story 2** → risk judgment + Responsible AI.
- **Story 3** → engineering restraint + you actually understand the retrieval tech.
- Together: *"I know the fancy techniques cold, and I know when* not *to use them."* — a Staff-level signal.
