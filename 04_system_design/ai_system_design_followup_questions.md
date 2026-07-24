# AI System Design Interview — Follow-Up Questions

> Drawing the architecture gets you through the first few minutes.
> Defending every design decision is what gets you hired.

---

## 🧠 LLM Selection

- Why did you choose GPT, Claude, Gemini, or an open-source model?
- Why not a smaller model?
- When would you fine-tune instead of using RAG?
- How do you reduce hallucinations?
- How do you ensure consistent outputs?

---

## 📚 RAG

- Why RAG instead of fine-tuning?
If the information chnages fast RAG is better choice then fine tunning
- How do you chunk documents?



- Which embedding model would you choose and why?

- How do you handle duplicate or conflicting documents?
- How do you improve retrieval precision?
- What happens if retrieval returns irrelevant context?
- How would you evaluate retrieval quality?

---

## ⚡ Performance & Scalability

- How would you reduce latency?
- Where would you introduce caching?
- How would the system handle 10,000 concurrent users?
- Which components would you scale independently?
- What happens if the vector database goes down?
- How do you design graceful fallbacks?

---

## 💰 Cost Optimization

- How do you reduce token usage?
- When should you switch to a smaller model?
- How do you minimize embedding costs?
- How would you track cost per user or per request?
- Which requests don't need an LLM at all?

---

## 🔒 Security & Production

- How do you prevent prompt injection?
- How do you prevent sensitive data leakage?
- How do you implement authorization for enterprise documents?
- How do you handle PII before sending data to an LLM?
- How do you version prompts safely?

---

## 📊 Evaluation & Monitoring

- What metrics would you monitor in production?
- How do you measure answer quality?
- How do you detect hallucinations?
- How would you run A/B tests on prompts or models?
- How do you know a model update actually improved the system?

---

## 🚨 Failure Scenarios

- What if the LLM API is down?
- What if the vector database is unavailable?
- What if retrieved context is outdated?
- What if response time suddenly doubles?
- How do you debug incorrect AI responses in production?
