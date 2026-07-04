# System Design Interview Roadmap — 25 Must-Do Questions (2026)

A practical tiered roadmap for system-design prep. Source infographic: `learn.jpg`
(DesignGurus.io). Work top-down — master T1 before T2, etc. Check off as you can whiteboard
each one end to end (requirements → API → data model → scale → tradeoffs).

> **For your level (Staff / Principal AI-Data):** T2 is where most prep should live, but
> **T3 (AI/real-time) and T5 (case studies)** are your differentiators — read T5 like papers,
> not problems. T3 directly matches the AI-platform roles you're targeting.

---

## T1 · Warm-ups
*Foundational, single-concept problems. Master these first.*

- [ ] Design TinyURL
- [ ] Design Pastebin
- [ ] Design an API rate limiter
- [ ] Design a unique ID generator
- [ ] Design typeahead / autocomplete suggestion

## T2 · The Classics
*The must-know FAANG canon. Where most of your prep should live.*

- [ ] Design Twitter
- [ ] Design Instagram
- [ ] Design Facebook Messenger
- [ ] Design the Uber backend
- [ ] Design Yelp / Nearby Friends

## T3 · Modern Systems
*Where 2026 interviews are heading. Real-time, AI, and collaborative tools.*

- [ ] Design ChatGPT
- [ ] Design Discord
- [ ] Design Google Docs
- [ ] Design a notification system
- [ ] Design Netflix recommendations

## T4 · Heavy Hitters
*Senior+ territory. Storage internals, payment correctness, low-latency systems.*

- [ ] Design YouTube / Netflix
- [ ] Design Amazon S3
- [ ] Design a payment system
- [ ] Design Google Search
- [ ] Design a stock exchange

## T5 · Case Studies
*For staff and principal interviews. Read these like papers, not problems.*

- [ ] Amazon Dynamo
- [ ] Apache Kafka
- [ ] Apache Cassandra
- [ ] Google File System (GFS)
- [ ] Google BigTable

---

## How to practice each one (the framework)
1. **Clarify requirements** — functional + non-functional (scale, latency, consistency).
2. **Estimate** — QPS, storage, bandwidth (back-of-envelope).
3. **API design** — the core endpoints.
4. **Data model** — SQL vs NoSQL, schema, partitioning key.
5. **High-level architecture** — draw the boxes (LB, services, cache, DB, queue).
6. **Deep-dive** — pick the 1–2 hardest parts and go deep (the interviewer's real test).
7. **Scale & tradeoffs** — bottlenecks, caching, sharding, replication, CAP tradeoffs.
8. **Wrap up** — failure modes, monitoring, what you'd do with more time.

## Cross-references in this folder
- `rate_limiters/` — your existing rate-limiter implementations (covers T1 #3).
- `file_transfer/` — file-tracking design practice.
- See also `../06_study_plans/` for the broader prep plans.
