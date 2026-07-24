# Bootcamp Notebooks — Consolidated Notes

One place to review learnings and pointers across every notebook in this folder, instead of re-reading all the code each time. Pair this with the "Cheat sheet" cell added inside [day7_lab_alignment_loop.ipynb](day7_lab_alignment_loop.ipynb) for the deep-dive tuning-loop skeleton.

## Notebook index

| Notebook | Day | Goal (one line) | Domain / data |
|---|---|---|---|
| [day1_labA_classical_decisions.ipynb](day1_labA_classical_decisions.ipynb) | 1A | Train 3 classical models, compare with honest metrics, tune the decision **threshold** to a business budget. | Telco churn (`../datasets/`) |
| [day1_labB_pytorch_mlp.ipynb](day1_labB_pytorch_mlp.ipynb) | 1B | Build an MLP in PyTorch; run the canonical **forward → loss → backprop → step** loop; watch regularization fight overfitting. | Telco churn (same data as 1A) |
| [day2_lab_transformers.ipynb](day2_lab_transformers.ipynb) | 2 | See **tokens → embeddings → attention** inside a real transformer; compare classical vs. transformer features on the same task (quality/latency/cost trade-off). | Text classification |
| [day3_lab_finetune.ipynb](day3_lab_finetune.ipynb) | 3 | Fine-tune tiny **distilGPT2** on support text; watch the loss curve; deliberately trigger + recover from a **loss spike**; compare generations before/after; peek at reduced precision for deployment. | Customer-support text |
| [day4_lab_eval_sft_data.ipynb](day4_lab_eval_sft_data.ipynb) | 4 | Eval-first SFT: baseline-generate on support/incident/tool-use examples, apply data gates, then run a tiny SFT update. | Support/incident/tool-use examples |
| [day5_RHL_lab_preference_dpo_grpo.ipynb](day5_RHL_lab_preference_dpo_grpo.ipynb) | 5 | Minimal **DPO-style** preference tuning: chosen-vs-rejected log-prob margin, before vs. after. | Chosen/rejected preference pairs |
| [day6_RHL_lab_judge_calibration.ipynb](day6_RHL_lab_judge_calibration.ipynb) | 6 | Tune a small LM to act as a **PASS/FAIL judge**, calibrated against human labels. | 5 human-labeled candidate answers |
| [day7_lab_alignment_loop.ipynb](day7_lab_alignment_loop.ipynb) | 7 | End-to-end **alignment loop**: generate → score with a reward function → SFT-tune → re-evaluate → test generalization. | 3 production-style tasks + reward() |

## The recurring skeleton (day3, day5, day6, day7 all share this shape)

```
load_model()  →  freeze_most_weights()  →  compute_loss(mask_prompt)  →  train_loop()  →  eval_before/after()  →  compare
```

| Block | Why | Where it differs by notebook |
|---|---|---|
| Load model | Get a small CPU-friendly model + tokenizer, with a fallback model if download fails. | Same pattern everywhere (`load_small_lm`). |
| Freeze most weights | Full fine-tuning is slow/unstable on CPU with tiny data; only unfreeze a small slice. | day3/day6: `lm_head`/`embed_tokens` keywords. day7: top-K transformer blocks + head (untied LM head). day5: same keyword approach, used inside a DPO loss instead of plain SFT loss. |
| Compute loss | Mask the prompt with `-100` so only the target/answer tokens are scored. | day3/day6/day7: plain cross-entropy SFT loss. day5: **DPO loss** — compares chosen vs. rejected log-prob margin through a sigmoid, not just next-token cross-entropy. |
| Train loop | `backward()` computes gradients (which way reduces loss); `opt.step()` nudges weights that way. | day7 accumulates gradients over the whole batch per epoch (smoother loss); day3/day5/day6 step per single example. |
| Eval before/after | Run the *same* generation + scoring function twice (before and after tuning) so the comparison is fair. | day3/day6: PASS/FAIL accuracy. day5: chosen>rejected win-rate. day7: reward() score. |
| Compare + stress-test | Look at loss trend + score/accuracy/reward trend; test a held-out example to catch memorization vs. real learning. | Only day7 has an explicit held-out generalization cell (Section 5, `new_task`). Worth trying in day5/day6 too. |

## Per-notebook pointers & gotchas

- **day1_labA** — the real lesson is picking a **threshold**, not just accuracy: a model with lower raw accuracy can be the right choice if it fits the business's false-positive/false-negative budget.
- **day1_labB** — watch the loss *curves* (train vs. val) to see overfitting appear before you look at any single accuracy number; regularization (dropout/weight decay) is the fix being demonstrated.
- **day2** — the "bake-off" is the point: transformer embeddings usually win on quality but cost more latency — decide Keep/Augment/Replace based on the numbers, not by default preference for the fancier model.
- **day3** — the deliberate loss spike is intentional pedagogy: too-high learning rate breaks training, and recovering from it (lowering lr / resuming from checkpoint) is the actual skill being taught, not just "fine-tuning works."
- **day4** — "eval-first" means data gates run *before* SFT — bad/ungrounded examples get filtered out before they ever get trained on. This ordering matters more than the SFT step itself.
- **day5** — the trainable DPO loss line is `margin = beta * (lp_c - lp_r)` (simplified, reference-free version); the commented-out line above it shows the "real" DPO formula which also subtracts each side's frozen reference-model score — worth uncommenting to compare.
- **day6** — `parse_label`'s string-matching is a fragile classifier; if you see lots of `UNKNOWN` predictions, that's a parsing problem, not necessarily a model-quality problem.
- **day7** — reward is deliberately computed on the **completion only**, never prompt+completion (scoring the prompt too pins reward at a constant 1.0 and hides all signal) — see the notebook's own "four fixes" list at the top for the other three non-obvious details.

## Glossary (terms worth being able to explain from memory, no notes)

- **Seed** (`random.seed()`, `torch.manual_seed()`) — fixes the "shuffle order" of pseudo-randomness so re-runs are reproducible; Python's `random` and PyTorch's RNG are independent, so both need seeding.
- **Epoch** — one full pass over the entire training set; `epochs=N` means the data is looped over N times before you stop.
- **Loss** — a single number measuring how wrong the model's predictions were (cross-entropy for next-token prediction); computed by comparing predicted probabilities to the true `labels`.
- **Label masking (`-100`)** — marks positions cross-entropy loss should ignore (e.g., prompt tokens), so the model is only scored on the part it's actually supposed to generate.
- **Freeze / unfreeze (`requires_grad`)** — freezing a parameter means the optimizer will never update it; only unfrozen ("trainable") parameters get nudged during training.
- **Gradient** — the slope of the loss with respect to each weight; tells the optimizer which direction to nudge that weight to reduce loss (computed via `.backward()`).
- **Gradient descent** — repeatedly nudging weights a small step in the direction that reduces loss, over many iterations.
- **Reward function** — an automatic scorer (plain code, not a model) used to grade generated text against a rubric (e.g., keyword coverage, verbosity penalty).
- **DPO margin** — `log P(chosen) - log P(rejected)`; a positive, growing margin after tuning means the model increasingly prefers the chosen answer over the rejected one.
- **Judge model** — a separate model trained specifically to output a PASS/FAIL (or similar) verdict on other models' outputs — distinct from tuning the answer-generating model itself.
- **Generalization vs. memorization** — generalization means the model learned the underlying *pattern*; memorization means it only reproduces the exact training examples. Tested with held-out examples never seen during training.
- **ROC-AUC** *(from day1)* — area under the ROC curve; measures how well a model separates two classes across all thresholds, not just one fixed cutoff.

---
*This file is a living summary — update it as new notebooks are added or as pointers change.*
