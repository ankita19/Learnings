# Event-Driven Agentic Platform — End-to-End System Design

## 1. Problem Statement

Design an event-driven agentic platform that can autonomously orchestrate multi-step AI workflows.

**Functional Requirements**
1. Process thousands of concurrent events
2. Agents act autonomously (react to events, decide next steps)
3. Maintain state across long-running tasks (minutes to hours/days)
4. Handle failures gracefully
5. Scale to thousands of concurrent agent executions

**Non-Functional Requirements**
- High concurrency, horizontal scalability
- Low latency for interactive workflows
- Durability — no lost work on crash
- Observability — every workflow must be debuggable
- Multi-tenant safe (isolation, rate limits)

---

## 2. High-Level Architecture

```
                                   ┌─────────────────────┐
 Client / API caller  ───────────▶│   API Gateway        │
                                   │  (AuthN, RateLimit,   │
                                   │   Routing, Validation)│
                                   └──────────┬───────────┘
                                              │
                                              ▼
                                   ┌─────────────────────┐
                                   │   Event Bus (Kafka)   │
                                   │ partitioned by         │
                                   │ workflow_id            │
                                   └──────────┬───────────┘
                                              │
                                              ▼
                          ┌───────────────────────────────────┐
                          │     Orchestrator Service             │
                          │  (workflow state machine, durable    │
                          │   execution, one shard = 1 workflow) │
                          └──────────┬─────────────┬───────────┘
                                     │             │
                     dispatch task   │             │  read/write state
                                     ▼             ▼
                     ┌───────────────────┐   ┌───────────────────┐
                     │  Agent Worker Pool  │   │  State Store        │
                     │ (stateless, auto-   │   │ (Postgres/DynamoDB  │
                     │  scaling, per-agent │   │  + Redis cache)     │
                     │  type queues)       │   └───────────────────┘
                     └─────────┬──────────┘
                               │ emits completion / failure events
                               ▼
                        back onto Event Bus ──▶ Orchestrator consumes ──▶ next step

                     ┌───────────────────┐
                     │  Dead Letter Queue  │◀── exhausted retries
                     └───────────────────┘

                     ┌───────────────────┐
                     │  Observability      │◀── traces/metrics/logs from every hop
                     │ (OTel, Prometheus, │
                     │  Grafana, ELK)      │
                     └───────────────────┘
```

**Core idea:** the Event Bus decouples every component. Nothing calls anything else synchronously except the Gateway's initial request. Everything downstream reacts to events, which is what gives you the "thousands of concurrent events" and "autonomous" properties for free.

---

## 3. Component Breakdown

### 3.1 API Gateway
- TLS termination, JWT validation, per-tenant rate limiting (token bucket)
- Translates external REST/GraphQL request → internal event, publishes to bus, returns `workflow_id` immediately (202 Accepted pattern — don't block on the workflow)
- Exposes a status/polling endpoint and a WebSocket/SSE channel for streaming results back

### 3.2 Event Bus (Kafka / Pulsar / SQS+SNS)
- **Partition key = `workflow_id`** → all events for one workflow stay strictly ordered; different workflows parallelize across partitions
- Durable log with configurable retention → acts as your audit trail and replay mechanism
- Separate topics: `workflow.events`, `agent.tasks.<agent_type>`, `agent.results`, `workflow.dlq`

### 3.3 Orchestrator
- The brain. Implemented as a **durable state machine per workflow instance** (Temporal / AWS Step Functions / custom saga engine)
- Consumes events → looks up current state → runs transition logic → emits next task(s) → persists new state
- **Stateless process, stateful data** — the orchestrator pod itself holds nothing; ownership of a workflow partition is assigned via consumer-group rebalancing, so any orchestrator replica can pick up any workflow after a crash
- Deterministic replay: if it crashes mid-step, it recovers by replaying persisted events, not by trusting in-memory state

### 3.4 Agent Worker Pool
- Stateless executors, one pool per agent type, each pulling from its own task queue
- Horizontally auto-scaled on queue depth (KEDA / HPA)
- Each agent: pulls task → executes (LLM call, tool call, etc.) → emits `result` or `failure` event → never talks to another agent directly (always through the bus)

### 3.5 State Store
- **Redis**: hot path — current step, in-flight status, fast reads for the polling/status API
- **Postgres/DynamoDB**: durable system of record — full event history per `workflow_id`, used for recovery and audit
- Schema: `workflow_id → {status, current_step, context_blob, retry_count, updated_at, history_offset}`

### 3.6 Dead Letter Queue + Alerting
- After N retries with backoff, task moves to DLQ instead of blocking the partition
- On-call gets paged; workflow marked `failed_needs_intervention` rather than silently stuck

### 3.7 Observability
- Every event carries a `trace_id` propagated end-to-end (OpenTelemetry)
- Metrics: queue depth, per-agent latency (p50/p95/p99), retry rate, DLQ rate, tokens consumed/workflow
- Structured logs keyed by `workflow_id` so you can pull the full timeline of any single execution

---

## 4. State Management

Two complementary patterns, used together:

1. **Event Sourcing** — the source of truth is the append-only log of events; current state is derivable by replaying them. Gives you audit trail, time-travel debugging, and recovery for free.
2. **Snapshotting** — for long-running workflows, periodically checkpoint derived state so you don't replay thousands of events just to answer "where is this workflow right now?"

**State machine per workflow** (example):
```
PENDING → RUNNING → WAITING_ON_AGENT → RUNNING → ... → COMPLETED
                                     ↘ FAILED → RETRYING → COMPLETED
                                     ↘ FAILED → DLQ → MANUAL_INTERVENTION
```

Checkpoint **after every step**, not just at completion — this is what lets recovery resume mid-workflow instead of from scratch.

---

## 5. Failure Handling

| Failure Mode | Mitigation |
|---|---|
| Agent task fails transiently | Retry with exponential backoff + jitter |
| Agent task fails repeatedly | Move to DLQ after N attempts, alert, mark workflow for manual review |
| Duplicate task delivery (at-least-once bus) | Idempotency key per task; agent checks/sets before executing side effects |
| Orchestrator crashes mid-workflow | Another replica takes over the partition (consumer group rebalance), resumes from last persisted checkpoint |
| Multi-step workflow fails halfway with side effects already applied | **Saga pattern** — each step defines a compensating action; on failure, run compensations in reverse order |
| Agent hangs / never responds | Per-step timeout → escalate to fallback agent or human-in-the-loop queue |
| Event bus partition unavailable | Multi-AZ replication (Kafka ISR / Pulsar bookies); producer retries with idempotent producer config |

---

## 6. Latency Optimization

- **Stream, don't block**: gRPC streaming or SSE so partial LLM output reaches the client as it's generated
- **Parallelize independent steps** in the workflow graph instead of forcing a serial chain
- **Model cascading**: cheap/fast model for routing & classification, expensive model reserved for the step that needs it
- **Cache deterministic sub-results**: embeddings, retrieval, repeated tool calls
- **Pre-warm agent worker pools** to avoid cold-start latency at burst scale
- **Colocate orchestrator, state store, and bus** in the same region/AZ; only go cross-region for global failover
- **Connection pooling / keep-alive** between orchestrator and workers (gRPC channels reused, not recreated per call)

---

## 7. Protocol Choices

**Internal (orchestrator ↔ workers): gRPC**
- Binary, Protobuf-typed contracts, HTTP/2 multiplexing (no head-of-line blocking)
- Supports streaming (server/client/bidi) — useful for agents streaming partial LLM tokens back to the orchestrator
- Compile-time-safe schemas via `.proto` files, easy code-gen across languages

**External (client ↔ Gateway): REST/JSON or GraphQL**
- Broader client compatibility, easier debugging, standard tooling

**Auth tokens (JWT) at the Gateway**
- Client authenticates once → signed JWT with claims (identity, scopes, expiry)
- Gateway validates signature + expiry locally, no DB round-trip per request → keeps the edge fast

**LLM tokens (inside agents)**
- Unit of text consumed/produced by model calls
- Drives three engineering decisions: (1) context truncation/summarization before handing history to an agent, (2) per-workflow token budget tracking for cost control, (3) streaming tokens back is a real latency lever, not just UX polish

---

## 8. Scalability Levers

- **Horizontal scaling**: Gateway, Orchestrator, and Agent Workers are all stateless — scale by adding replicas
- **Partitioning**: bus partitioned by `workflow_id` bounds ordering to a single workflow, lets partitions scale independently
- **Backpressure**: rate-limit at the Gateway; queue depth-based autoscaling on workers so a burst doesn't cascade into a crash
- **Multi-tenancy isolation**: per-tenant rate limits + separate queues/partitions for noisy-neighbor protection

---

## 9. Trade-offs Worth Naming in the Interview

- **Event sourcing adds complexity** (replay logic, schema evolution of events) in exchange for auditability and recoverability — worth it here because workflows are long-running and failures must be debuggable.
- **At-least-once delivery** (Kafka default) is simpler to operate than exactly-once, but pushes idempotency responsibility onto agents — a deliberate trade favoring throughput and simplicity.
- **Saga pattern over 2PC**: distributed transactions across agents/tools aren't practical at this scale; compensating actions are eventually consistent but don't block the whole system.
- **Stateless orchestrator replicas** cost you a bit of latency (state store round-trip per step) in exchange for crash resilience and horizontal scale.

---

## 10. Follow-up: What if you need to process real-time events?

The design above optimizes for durability and correctness over long-running workflows — but "real-time" (sub-second reaction, streaming decisions) needs a few deliberate additions on top:

**Split the workload into two lanes**
- **Hot path (real-time)**: low-latency, in-memory, best-effort-durable — for events that need a reaction in milliseconds (e.g. a live sensor reading, a user action, a market tick)
- **Cold path (durable)**: the orchestration flow already designed — for multi-step, stateful, long-running agent workflows

Route incoming events at the Gateway based on a `latency_class` flag or event type, rather than forcing everything through the same durable pipeline.

**Changes needed for the hot path**

| Concern | Batch/Durable Design (above) | Real-Time Addition |
|---|---|---|
| Transport | Kafka topic, consumer polls | Stream processor (Kafka Streams / Flink) or in-memory pub/sub (Redis Streams, NATS) for sub-ms hop latency |
| Agent dispatch | Queue → worker pool | Keep a **warm pool** of agents subscribed directly to the stream — no cold start, no queue wait |
| State reads | Postgres + Redis cache | Read exclusively from **Redis/in-memory state**, async-write-behind to Postgres for durability (don't block the hot path on a DB write) |
| Decisioning | Full orchestrator state machine per event | Lightweight **rules/streaming engine** (CEP — complex event processing) for fast-path decisions; only hand off to the full orchestrator if the event triggers a multi-step workflow |
| Windowing | N/A | Time/sliding windows (Flink/Kafka Streams) for aggregation cases — e.g. "3 anomalies in 10 seconds → trigger agent" |
| Backpressure | Queue depth-based autoscaling | **Load shedding** — if the stream processor falls behind, drop or sample low-priority events rather than adding latency to everything |

**Concrete pattern**
```
Real-time source ──▶ Stream Processor (Flink/Kafka Streams)
                         │
                         ├─ simple reaction ──▶ Warm agent pool ──▶ immediate response (SSE/WebSocket to client)
                         │
                         └─ needs multi-step workflow ──▶ hand off event to Orchestrator (durable lane, as designed in §3)
```

**Key trade-off to state out loud in the interview**: real-time processing trades durability guarantees for latency — you accept some risk of dropped/lost or eventually-persisted events in exchange for millisecond reaction time. The durable orchestrator lane stays the source of truth for anything that must not be lost; the real-time lane is "fast and best-effort," escalating to the durable lane only when a real multi-step workflow needs to start.

---

## 11. One-Sentence Summary (for whiteboard recall)

> Client requests fan out through a partitioned event bus to a durable, replayable orchestrator state machine, which dispatches idempotent tasks to stateless autoscaled agent workers over gRPC, checkpoints state after every step, and uses sagas + DLQs to fail gracefully at thousands-of-concurrent scale.
