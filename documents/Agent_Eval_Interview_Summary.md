# Engage Agent Migration Eval — Summary & Interview Talking Points

## Plain-English Summary

**The question:** Should the "Engage" agent (drafts follow-up emails to sales leads) migrate from its current hand-written orchestration to a new platform called Dracarys? Both versions use the same retrieval method, so this test isolates *only* the orchestration change — a clean A/B, not a confounded one.

**The method:** 232 realistic synthetic sales leads, each agent drafted a response 3 separate times (to test consistency), and every draft was scored independently by **two different judge models** (Claude Opus and GPT-5-mini), each judge run 3 times per draft (to test the judge's own reliability). That's ~8,300 total judge calls. Scoring used a 12-point rubric (5 "gating" pass/fail criteria + 7 quality signals), plus two extra add-on checks: groundedness and citation accuracy.

**The verdict:** **Proceed with the migration**, with one known fix needed. Both judges agree Dracarys is never worse than the current system — one judge says it's a clear statistical win (+15.5 points), the other says it's a statistical tie (non-inferior, +3.0 points, not a loss). Dracarys wins decisively on writing quality, personalization, and — most importantly — on correctly knowing *when to hand a conversation to a human* instead of guessing. Its one weakness: on questions it should answer, it sometimes paraphrases numbers instead of quoting the source documents exactly.

---

## Why This Is a Strong Interview Example

This single study demonstrates almost every dimension a Director-level interviewer wants to see in an "evaluation framework" story:

| Skill being demonstrated | Where it shows up in the study |
|---|---|
| Designing a **controlled experiment**, not just "did it seem good" | Holding retrieval constant to isolate the orchestration variable |
| Handling **judge/LLM unreliability**, not trusting a single model's opinion | Two independent judges, each rolled 3x, explicit inter-judge agreement (Cohen's κ) |
| **Statistical rigor**, not "it looked better" | Paired confidence intervals, non-inferiority margin, effect sizes |
| **Separating measurement reliability from product reliability** | The judge-variance vs. agent-variance framework (§3.2) — "is this a broken thermometer or a genuinely inconsistent product?" |
| **Root-causing a failure**, not just reporting a score | Answer-equivalence gap traced to two specific behaviors (loose figures, over-cautious hand-off), with a proposed fix and expected impact (+45pp) |
| Knowing **what NOT to over-index on** | Explicitly calling personalization "the softest number" because the judge itself is noisy there |
| **Actionable recommendation**, not just data | "Proceed, with fix X and Y" — a decision, not a data dump |

---

## Key Numbers to Have Ready (memorize these 5)

1. **232 leads, 2 judges, 3 runs each** — the scale/rigor of the study
2. **+15.5 pp (statistically superior) / +3.0 pp (non-inferior)** — the two judges' verdicts; both support migrating, neither finds the new system worse
3. **65.5% vs 50.0%** — pass rate under the stricter judge (or **84.5% vs 81.5%** under the more lenient one)
4. **Hand-over accuracy: 87.9% vs 32.8%** — the single biggest win; the new system correctly recognizes when to route to a human far more often
5. **One clear weakness, one clear fix**: new system paraphrases numbers instead of quoting them verbatim → expected to close the entire respond-side gap (43% → 88%) if fixed

---

## How to Use This in an Interview

### If asked "walk me through an evaluation you designed"
Use the **structure**, not every number:
1. What decision were we trying to make? (migrate or not)
2. How did we isolate the variable we cared about? (held retrieval constant)
3. How did we handle the fact that LLM judges themselves are unreliable? (two judges, each rolled multiple times, checked their agreement)
4. What did we conclude, and how confident were we? (statistical test, not a gut call)
5. What's the one thing we'd fix before shipping, and how do we know that's the highest-leverage fix? (root-caused to one rubric, one behavior pattern)

### If asked "how do you know your evaluation itself is trustworthy?"
This is your best answer of all your prepped material. Use the **judge-variance vs. agent-variance framework**: "I always ask two separate questions — is my measuring stick reliable, and is the thing I'm measuring actually consistent? If I only look at the final score, I can't tell whether a low score means the product is bad or my judge is noisy. In this study, we found the judge was tight (re-scoring the same draft flipped the verdict only ~1 in 8 times) but the *product* had a real ~25% tail of run-to-run inconsistency — so we knew to go fix the agent's hand-off logic, not tune the eval."

### If asked "tell me about a time you had to make a tough call on 'good enough to ship'"
Use the **non-inferiority framing**: "Rather than requiring the new system to be strictly better everywhere, I designed the test as a non-inferiority question — is it at least as good, within a pre-set margin, allowing for a specific area where a fix is already scoped? That's a more honest way to evaluate a migration than demanding perfection on every dimension before shipping anything."

### If asked about handling disagreement/conflicting signals
Use the **two judges disagreeing on magnitude but agreeing on direction** point: "The two judges disagreed on how big the win was, but they never disagreed on the direction — neither one ever found the old system better. When your signals conflict on magnitude but agree on direction, that's usually strong enough to act on; when they conflict on direction itself, that's when I'd slow down and investigate the eval before trusting either number."

---

## One Caution

This is dense, detailed material — in an interview, **lead with the plain-English summary and the 5 key numbers**, and only go deeper into methodology (judge variance, statistical tests, root-cause analysis) if the interviewer asks a follow-up that invites it. Dumping the full rigor unprompted will read as overexplaining rather than confidence.
