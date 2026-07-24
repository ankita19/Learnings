# Week 1 Setup & Prep — read before Day 1

Welcome to **Week 1: Modeling Foundations & Adaptation** of the CxAI AI Upskill Program.
This guide gets your **local machine** ready **before** Day 1 so we can spend class time learning.

Everything runs **CPU-only** — no GPU required. Budget **~20 minutes**, and do it **the day before** the
session. If anything fails, ping the cohort channel early so we can help.

---

## Schedule

| Day | Date | Topic |
|-----|------|-------|
| 1 | **Wed Jul 15** | Classical ML + Neural Foundations |
| 2 | **Thu Jul 16** | Transformer Foundations |
| 3 | **Fri Jul 17** | Adapting Pretrained Models |


---

## Prerequisites

- **Python 3.12** (matches the class environment). Check with `python --version`.
- **Git** (to clone the repo) — or a copy of the `CxAI-Bootcamp/` folder.
- **~5 GB free disk** (packages + model caches).
- Works on **Windows, macOS, or Linux**.

---

## 1. Get the materials

```bash
# if using git (sparse-checkout the bootcamp folder only):
git clone --filter=blob:none --no-checkout https://microsoft.ghe.com/bic/cxai_coreai_lab.git
cd cxai_coreai_lab
git sparse-checkout set --no-cone CxAI-Bootcamp
git checkout
cd CxAI-Bootcamp
```

## 2. Create and activate a virtual environment

**macOS / Linux**
```bash
python3.12 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

> Keep this environment activated whenever you work on Week 1 material.

## 3. Install the pinned dependencies

```bash
python -m pip install --upgrade pip
pip install -r setup/requirements.txt
```
> `torch==2.3.1` installs the **CPU** build automatically — no CUDA needed.


## 4. Verify — run the smoke test

```bash
jupyter lab
```
Open **`setup/smoke_test.ipynb`** → **Run All**. It imports every package, prints versions, loads both
datasets, and runs one forward pass through a cached model.
**Your setup is good only when every cell is green.**

---

## What you'll run each day

Lab notebooks live in **`notebooks/`**. Launch Jupyter from the repo root (or from `notebooks/`) and open them there:

| Day | Notebook(s) |
|-----|-------------|
| 1 | `day1_labA_classical_decisions.ipynb`, `day1_labB_pytorch_mlp.ipynb` |
| 2 | `day2_lab_transformers.ipynb` (tokenize → embeddings/attention → classical-vs-LLM bake-off) |
| 3 | `day3_lab_finetune.ipynb` (fine-tune distilGPT2 → loss curve & spike → compression) |

The notebooks contain `# TODO` blanks we fill in together during class. 


---

## Troubleshooting

| Symptom | Fix |
|---|---|
| `python: command not found` or wrong version | Use `python3.12` / `py -3.12`. Confirm with `python --version` → should be 3.12.x. |
| `pip install` fails on `torch` | Make sure pip is current (`python -m pip install --upgrade pip`). The CPU wheel is large — let it finish. |
| Notebook can't find a dataset (`FileNotFoundError`) | Confirm you launched Jupyter from the `CxAI-Bootcamp/` directory and that the `datasets/` folder exists next to `setup/`. |
| Wrong kernel / packages "not found" in Jupyter | Ensure your `.venv` is **activated** before launching `jupyter lab`, so the notebook uses that interpreter. |

---

## Before Day 1 — quick checklist

- [ ] Python **3.12** virtual environment created and activated
- [ ] `pip install -r setup/requirements.txt` completed
- [ ] Datasets present in `datasets/`
- [ ] `setup/smoke_test.ipynb` runs **all green**

Questions before we start? Drop them in the cohort channel. See you **Wednesday, Jul 15**.
