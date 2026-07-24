# Week 1 Datasets — Sources & Citations

All datasets used in Week 1 are **public** and **synthetic or anonymized** (no real customer PII).
Both map to the cohort's **Sales / Customer Service** domain.

---

## 1. `telco_customer_churn.csv` — tabular (Day 1 & Day 2)

Customer-level telco account data used for **regression** (predict customer value /
`TotalCharges`) and **classification** (predict `Churn`). ~26.5% churn rate makes it a clean
teaching example for **class imbalance, precision/recall, and ROC-AUC**.

- **Rows / cols:** 7,043 × 21
- **Target(s):** `Churn` (Yes/No) for classification; `TotalCharges` / `MonthlyCharges` for regression
- **Source:** IBM "Telco Customer Churn" sample dataset (IBM Cognos Analytics sample).
- **Retrieved from:** IBM `telco-customer-churn-on-icp4d` GitHub repo —
  https://github.com/IBM/telco-customer-churn-on-icp4d (file: `data/Telco-Customer-Churn.csv`)
- **Also widely mirrored on Kaggle:** "Telco Customer Churn" by BlastChar —
  https://www.kaggle.com/datasets/blastchar/telco-customer-churn
- **License / terms:** IBM sample data, provided for public/educational use.
- **Citation:** IBM. *Telco Customer Churn* (IBM Cognos Analytics sample dataset). IBM, 2019.

## 2. `support_tickets_sample.csv` — text (Day 2)

A 40-row sample (4 per category × 10 categories) of **customer-support utterances** used for
**tokenization, embeddings, and attention visualization**. Sampled from the Bitext synthetic
customer-support dataset.

- **Columns:** `customer_message`, `category`, `intent`
- **Source:** Bitext — *Customer Service Tagged Training Dataset for LLM-based Virtual Assistants*
  (hybrid **synthetic** data; no real customer PII).
- **Retrieved from:** Hugging Face —
  https://huggingface.co/datasets/bitext/Bitext-customer-support-llm-chatbot-training-dataset
  (file: `Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv`)
- **License:** CDLA-Sharing-1.0 (Community Data License Agreement – Sharing 1.0).
- **Citation:** Bitext Innovations. *Customer Service Tagged Training Dataset for LLM-based
  Virtual Assistants*. Hugging Face, 2023.
- **Note:** Some original utterances contain templated placeholders (e.g. `{{Account Type}}`).
  The Day 3 notebook also includes a few hand-picked clean sentences for the clearest attention plots.

## 3. `support_tickets_classification.csv` — text (Day 2 bake-off & Day 3 fine-tune)

A balanced 640-row set (80 rows × 8 categories) of **customer-support utterances labeled by
category**, used for the **classical-vs-LLM bake-off** (TF-IDF+LogReg vs transformer-embeddings+LogReg),
and **reused in the Day 3 fine-tuning lab** (reformatted into `Customer: … / Support: …` examples).

- **Columns:** `text`, `category` (ACCOUNT, ORDER, REFUND, INVOICE, CONTACT, PAYMENT, CANCEL, DELIVERY)
- **Source / license / citation:** same Bitext dataset as `support_tickets_sample.csv` above
  (CDLA-Sharing-1.0; Bitext Innovations, Hugging Face, 2023).
