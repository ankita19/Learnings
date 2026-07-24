# My Framework for Evaluating Agent Quality
*(Methodology only — extracted from real evaluation work, generalized for interview use)*

---

## The One-Breath Version (say this first, then let them ask for depth)

"I think about agent evaluation in five layers: define what 'correct' means with a gold-standard rubric, separate gating criteria from quality signals, use multiple independent judges instead of trusting one, measure both the judge's reliability and the agent's consistency separately, then run the comparison as a statistical test — not a vibe check — before making a ship/no-ship call."

That's your anchor sentence. Everything below is what you unpack if they ask "tell me more" or "walk me through that."

---

## Layer 1 — Define Ground Truth Before You Score Anything

You can't evaluate an agent against "did it seem good" — you need a **gold-standard expected output** for each test case, built independently of the agent being tested.

- Build a rubric of specific, checkable rules — not one vague "quality" score. Split rules into:
  - **Gating rules** (must-pass, binary): the things that make an output actually wrong if violated — e.g., "did it make the same escalation/hand-off decision as the gold," "did it cover the customer's actual questions," "did it stay within formatting constraints."
  - **Signal rules** (quality, non-blocking): things that matter but shouldn't single-handedly fail an otherwise-correct response — tone, personalization, adaptability.
- This split matters because it lets you answer two different questions cleanly: *is this output acceptable to ship* (gating) vs. *is this output excellent* (signal). Conflating them either makes your bar too soft (bad output ships because it "felt" fine) or too strict (good outputs get rejected over polish).

**How I'd say it:** "The first design decision is separating 'must be correct' from 'nice to be great.' If everything's one blended score, you can't tell whether a low score means the agent is wrong or just plain-spoken."

---

## Layer 2 — Never Trust a Single Judge

An LLM judge is itself a noisy instrument — it can disagree with itself on a re-roll of the exact same input.

- Use **two independent judge models**, not one, ideally from different model families so their failure modes don't correlate.
- Run each judge **multiple times** on the same output ("rolls") to measure the judge's own consistency — if a judge flips its verdict on a re-roll, that's measurement noise, not signal.
- Take the **median or majority vote** across rolls per judge ("de-rolling") before trusting a single verdict.
- Report **inter-judge agreement** (e.g., Cohen's kappa) — if two reasonable judges agree most of the time, your eval is trustworthy; if they diverge sharply, that tells you *where* your rubric or gold standard is ambiguous, which is itself useful information.

**How I'd say it:** "I never take a single LLM judge's word for it. I run at least two independent judges, and I roll each one multiple times on the same output, because a judge that flips its own verdict on a re-roll can't be trusted to compare two agents fairly."

---

## Layer 3 — Separate "Is My Ruler Reliable" from "Is the Agent Reliable"

This is the sharpest, most senior-sounding part of the framework — most people conflate these two questions.

- **Judge variance** = re-score the *same* output multiple times with the *same* judge. High variance here means your measuring instrument is broken — fix the rubric or prompt before trusting any comparison.
- **Agent variance** = generate multiple *outputs* for the same input and score each once. High variance here means the *product* is inconsistent — that's a real finding about the agent, not the eval.
- You need both numbers before you can act. A low score could mean either "bad agent" or "bad ruler," and they require completely different fixes.

**How I'd say it:** "I always separate two questions: is my measuring stick reliable, and is the thing I'm measuring actually consistent? If I only look at a final score, I can't tell whether a low number means the agent is bad or my eval is noisy — and those require completely different fixes."

---

## Layer 4 — Compare Agents as a Statistical Test, Not a Score Diff

Once you trust the measurement, the actual A/B comparison needs real statistical discipline, especially for a "should we ship/migrate" decision:

- Frame it as the right *kind* of question: is this a **non-inferiority** test (is the new thing at least as good, within an acceptable margin) or a **superiority** test (is it strictly better)? Most migration decisions are non-inferiority questions, not superiority ones — you're often willing to ship something that's "not worse," not only something that's "definitively better."
- Use **paired comparisons** (same test case, both agents) rather than comparing aggregate averages independently — it controls for case-by-case difficulty differences.
- Report a **confidence interval**, not just a point estimate, and pre-register your acceptance margin before you see the results, so you're not moving the goalposts after the fact.

**How I'd say it:** "I frame agent comparisons as a proper statistical test — usually non-inferiority, since most real decisions are 'is the new version at least as good,' not 'is it perfect.' I use paired comparisons on the same test cases, and I set my acceptance margin before I look at the results, not after."

---

## Layer 5 — Root-Cause the Gap, Don't Just Report the Score

A number alone doesn't tell you what to fix.

- When an agent underperforms on a specific rubric, **decompose the failures into distinct behavioral patterns** — not every low score has the same cause. (e.g., "wrong answer" vs. "over-cautious deferral" vs. "right answer, wrong number" are three different bugs requiring three different fixes.)
- Quantify what share of the gap each pattern explains, so you can prioritize the fix with the highest leverage — the goal is finding the one or two changes that close most of the gap, not a laundry list.
- Validate the fix's *expected* impact before building it — e.g., "if we fix pattern X, which explains 80% of the failing cases, we'd expect the pass rate to rise from A% to B%."

**How I'd say it:** "I don't stop at a failing score — I break the failures into distinct behavior patterns and quantify how much of the gap each one explains, so the fix targets the highest-leverage pattern instead of a vague 'improve quality' effort."

---

## Bonus Layer — Add-On Signals That Don't Gate, But Still Matter

Some quality dimensions are worth tracking even if they shouldn't block a ship decision on their own — e.g., factual groundedness (are claims actually supported by source material) and citation accuracy (did it reference the right source). Keep these as **separate, non-gating signals** so they inform the roadmap without creating false failures on outputs that are otherwise correct.

**How I'd say it:** "I also track signals like groundedness and citation accuracy separately from the pass/fail gate — they matter for the roadmap, but I don't want a good, correct answer failing the eval because of a secondary metric."

---

## If They Push for a Concrete Example

Have this one-liner ready to bridge into a real story: *"I used exactly this framework recently to evaluate whether an agent should migrate to a new orchestration platform — two judges, reliability checks on both sides, and a root-caused, prioritized fix list before we made the call."* Then let them ask for detail rather than volunteering the full case study unprompted.

---

## Quick-Recall Skeleton (memorize this shape, not the prose)

1. **Define correctness** — gold standard + gating vs. signal rubric split
2. **Distrust single judges** — multiple judges, multiple rolls, de-roll to a verdict
3. **Separate ruler-reliability from product-reliability** — judge variance vs. agent variance
4. **Compare statistically** — non-inferiority framing, paired tests, pre-set margins
5. **Root-cause, don't just score** — decompose failures into fixable patterns, prioritize by leverage
6. *(Bonus)* Track non-gating signals (groundedness, citations) separately from the pass/fail bar
