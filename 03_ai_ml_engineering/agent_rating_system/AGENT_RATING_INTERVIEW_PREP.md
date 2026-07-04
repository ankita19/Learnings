# Atlassian - Support Agent Rating System Interview Prep

## Problem Statement

Design a system to manage support agent ratings:

**Requirements:**
1. Each support agent has an ID
2. Agents receive ratings from 1-5
3. Must support:
   - Recording ratings
   - Computing average rating
   - Sorting agents by average rating
   - Tie-breaking logic

**Follow-up:** How would you modify the design to support weighted votes?

---

## Interview Approach (Principal Backend Engineer Level)

### 1. Clarify Requirements (3-5 minutes)

**Critical questions to ask:**

#### Data & Scale
- How many agents? (hundreds, thousands, millions?)
- How many ratings per agent? (average and max)
- Are ratings historical or real-time?
- Do ratings have timestamps?
- Can ratings be deleted or modified?

#### Tie-Breaking
- What's the tie-breaking priority?
  - Agent ID (lexicographic)?
  - Total number of ratings (more is better)?
  - Most recent rating?
  - Highest individual rating ever received?

#### Output Requirements
- Just sorted list, or need rankings (1st, 2nd, 3rd)?
- Need top-K agents only, or full sorted list?
- Need to query individual agent's average?
- Need to show rating distribution (histogram)?

#### Weighted Votes (Follow-up)
- What determines weight? (customer tier, issue priority, time decay?)
- Static weights or dynamic?
- How much more should weighted votes count?

### 2. Design Decisions (5 minutes)

#### Data Structures

**Option 1: Simple Hash Map**
```python
agents: Dict[str, List[int]]  # agent_id -> list of ratings
```
- ✅ Simple, easy to understand
- ✅ O(1) insertion
- ❌ O(n) to compute average each time
- ❌ Need to sort entire list for ranking

**Option 2: Agent Object (Recommended)**
```python
class Agent:
    agent_id: str
    ratings: List[int]
    # Can cache average, track stats, etc.
```
- ✅ Encapsulation and extensibility
- ✅ Can add caching, validation, etc.
- ✅ Professional OOP design
- ✅ Easy to extend with weights, timestamps

**Option 3: Pre-computed Averages (Optimization)**
```python
agents: Dict[str, Agent]
sorted_cache: List[Agent]  # Updated lazily
```
- ✅ O(1) to get sorted list if cached
- ❌ More complex to maintain
- ❌ Premature optimization for interviews

#### Sorting Strategy

**For full list:** O(n log n) sort
**For top-K:** O(n log k) heap - better if k << n

### 3. Code the Solution (15-20 minutes)

**Start with basic version, then extend:**

#### Phase 1: Basic Agent Class (5 min)
```python
class Agent:
    def __init__(self, agent_id: str):
        self.agent_id = agent_id
        self.ratings = []

    def add_rating(self, rating: int):
        if not 1 <= rating <= 5:
            raise ValueError("Rating must be 1-5")
        self.ratings.append(rating)

    def get_average_rating(self) -> float:
        if not self.ratings:
            return 0.0
        return sum(self.ratings) / len(self.ratings)
```

#### Phase 2: System Class (5 min)
```python
class AgentRatingSystem:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def record_rating(self, agent_id: str, rating: int):
        if agent_id not in self.agents:
            self.agents[agent_id] = Agent(agent_id)
        self.agents[agent_id].add_rating(rating)

    def get_average_rating(self, agent_id: str) -> Optional[float]:
        if agent_id not in self.agents:
            return None
        return self.agents[agent_id].get_average_rating()

    def get_sorted_agents(self) -> List[Agent]:
        agents = list(self.agents.values())
        return sorted(agents,
                     key=lambda a: (-a.get_average_rating(), a.agent_id))
```

#### Phase 3: Tie-Breaking Strategy (5 min)
```python
from enum import Enum

class TieBreakStrategy(Enum):
    AGENT_ID = "agent_id"
    TOTAL_RATINGS = "total_ratings"

def get_sorted_agents(self) -> List[Agent]:
    def sort_key(agent: Agent):
        avg = agent.get_average_rating()
        if self.tie_break == TieBreakStrategy.AGENT_ID:
            return (-avg, agent.agent_id)
        elif self.tie_break == TieBreakStrategy.TOTAL_RATINGS:
            return (-avg, -len(agent.ratings), agent.agent_id)
    return sorted(self.agents.values(), key=sort_key)
```

#### Phase 4: Weighted Ratings (Follow-up, 5-10 min)
```python
class WeightedAgentRatingSystem(AgentRatingSystem):
    def __init__(self):
        super().__init__()
        self.rating_weights: Dict[str, List[float]] = defaultdict(list)

    def record_rating(self, agent_id: str, rating: int, weight: float = 1.0):
        super().record_rating(agent_id, rating)
        self.rating_weights[agent_id].append(weight)

    def get_average_rating(self, agent_id: str) -> Optional[float]:
        if agent_id not in self.agents:
            return None
        agent = self.agents[agent_id]
        weights = self.rating_weights[agent_id]

        if not agent.ratings:
            return 0.0

        weighted_sum = sum(r * w for r, w in zip(agent.ratings, weights))
        total_weight = sum(weights)
        return weighted_sum / total_weight if total_weight > 0 else 0.0
```

### 4. Test Your Solution (5 minutes)

**Walk through test cases:**

```python
# Test 1: Basic functionality
system.record_rating("agent_001", 5)
system.record_rating("agent_001", 4)
assert system.get_average_rating("agent_001") == 4.5

# Test 2: Sorting
system.record_rating("agent_002", 3)
sorted_agents = system.get_sorted_agents()
assert sorted_agents[0].agent_id == "agent_001"  # Higher avg

# Test 3: Tie-breaking
system.record_rating("agent_003", 4.5)  # Same avg as agent_001
sorted_agents = system.get_sorted_agents()
# Should break tie by agent_id

# Test 4: Edge cases
assert system.get_average_rating("nonexistent") is None
empty_system.get_sorted_agents() == []

# Test 5: Weighted (if implemented)
weighted_system.record_rating("agent_001", 5, weight=2.0)
weighted_system.record_rating("agent_001", 3, weight=1.0)
# avg = (5*2 + 3*1) / 3 = 4.33
```

### 5. Complexity Analysis

**Time Complexity:**
- `record_rating()`: O(1)
- `get_average_rating()`: O(1) if cached, O(m) if computed (m = ratings per agent)
- `get_sorted_agents()`: O(n log n) where n = number of agents
- `get_top_k_agents()`: O(n log k) using heap

**Space Complexity:**
- O(n * m) where n = agents, m = average ratings per agent
- Weighted: Additional O(n * m) for weights

---

## Advanced Follow-up Questions

### Q1: "How would you handle 1 million agents?"

**Answer:**
- **In-memory**: Current solution works fine
  - 1M agents * 100 ratings * 12 bytes ≈ 1.2GB - fits in memory
- **Database**: Store in SQL with proper indexing
  ```sql
  CREATE TABLE ratings (
    agent_id VARCHAR(50),
    rating INT,
    weight FLOAT DEFAULT 1.0,
    timestamp TIMESTAMP,
    INDEX idx_agent (agent_id)
  );
  ```
- **Materialized view** for averages:
  ```sql
  CREATE MATERIALIZED VIEW agent_stats AS
  SELECT agent_id,
         AVG(rating * weight) / AVG(weight) as weighted_avg,
         COUNT(*) as total_ratings
  FROM ratings
  GROUP BY agent_id;
  ```

### Q2: "What if ratings come in at high velocity (1000/sec)?"

**Answer:**
- **Streaming processing**: Kafka + Stream processors
- **Eventual consistency**: Update rankings periodically, not on every vote
- **Write-through cache**: Redis for hot data, DB for persistence
- **Batch updates**: Collect ratings, update in batches
- **Approximate rankings**: If exact isn't needed, use sampling

### Q3: "How do you handle time-decay weights automatically?"

**Answer:**
```python
class TimeDecayWeightedSystem:
    def __init__(self, decay_rate=0.1):
        self.decay_rate = decay_rate  # Higher = faster decay

    def calculate_weight(self, timestamp, current_time):
        age_days = (current_time - timestamp) / 86400
        return math.exp(-self.decay_rate * age_days)

    def get_average_rating(self, agent_id, current_time=None):
        # Recalculate weights based on current time
        weights = [self.calculate_weight(ts, current_time)
                  for ts in agent.rating_timestamps]
        # Then compute weighted average
```

**Trade-offs:**
- ✅ Recent ratings automatically count more
- ✅ No manual weight specification
- ❌ Need to recompute for every query (can cache)
- ❌ Rankings change over time even without new ratings

### Q4: "What about removing outliers?"

**Answer:**
- **Approach 1: Trim extremes** (trim top/bottom 5%)
- **Approach 2: Winsorization** (cap extremes at percentile)
- **Approach 3: Median instead of mean** (resistant to outliers)
- **Approach 4: Weighted by confidence** (more ratings = more confident)

```python
def get_average_rating_trimmed(self, agent_id: str) -> float:
    ratings = sorted(self.agents[agent_id].ratings)
    trim = len(ratings) // 20  # 5%
    if trim > 0:
        ratings = ratings[trim:-trim]
    return sum(ratings) / len(ratings) if ratings else 0.0
```

### Q5: "How would you implement real-time leaderboard?"

**Answer:**
- **Redis Sorted Set**: Perfect for leaderboards
  ```python
  # Update score
  redis.zadd("agent_leaderboard", {agent_id: avg_rating})

  # Get top K
  redis.zrevrange("agent_leaderboard", 0, k-1, withscores=True)

  # Get agent rank
  redis.zrevrank("agent_leaderboard", agent_id)
  ```
- **Time complexity**: O(log n) updates, O(log n + k) top-K query
- **Benefits**: Fast, handles ties, persistent

### Q6: "What if you need percentile rankings instead of absolute?"

**Answer:**
```python
def get_percentile_rank(self, agent_id: str) -> float:
    """Return percentile (0-100) of this agent"""
    agent_avg = self.get_average_rating(agent_id)
    all_avgs = [a.get_average_rating() for a in self.agents.values()]

    count_below = sum(1 for avg in all_avgs if avg < agent_avg)
    return (count_below / len(all_avgs)) * 100 if all_avgs else 0.0
```

### Q7: "How do you ensure data consistency in distributed system?"

**Answer:**
- **Problem**: Multiple servers recording ratings, need consistent ranking
- **Solutions:**
  1. **Single source of truth**: Route all rating writes to primary
  2. **Event sourcing**: Append-only log, rebuild state
  3. **CRDT**: Conflict-free replicated data types
  4. **Eventually consistent**: Accept stale rankings for speed
  5. **Partitioning**: Shard by agent_id (each server owns subset)

---

## Key Differentiators for Principal Level

### What Makes a Principal-Level Answer:

1. **System Design Thinking**
   - Don't just code the algorithm
   - Think about production deployment
   - Consider monitoring, alerting, SLAs

2. **Trade-off Analysis**
   - Discuss accuracy vs performance
   - Consistency vs availability
   - Complexity vs maintainability

3. **Extensibility**
   - Design for future requirements
   - Clean abstractions (strategies, interfaces)
   - SOLID principles

4. **Scale Awareness**
   - Always discuss what breaks at scale
   - Know when to use DB vs cache vs in-memory
   - Understand distributed systems challenges

5. **Production Concerns**
   - Data validation and error handling
   - Testing strategy
   - Monitoring and observability
   - Disaster recovery

---

## Common Mistakes to Avoid

❌ **Don't:**
- Jump into coding without clarifying tie-breaking
- Use naive sorting for top-K (should use heap)
- Forget to validate rating range (1-5)
- Ignore edge cases (empty ratings, division by zero)
- Hardcode tie-breaking strategy
- Miss the weighted votes follow-up

✅ **Do:**
- Ask about tie-breaking upfront
- Use OOP with clean classes
- Validate inputs
- Use enums for strategies
- Explain time/space complexity
- Extend design for weighted votes

---

## Code Quality Checklist

- [ ] Type hints on all functions
- [ ] Input validation (rating range, non-null)
- [ ] Docstrings for classes and methods
- [ ] Clean variable names
- [ ] Separation of concerns (Agent vs System)
- [ ] Extensible design (easy to add features)
- [ ] Error handling with meaningful messages
- [ ] Complexity analysis documented

---

## Time Allocation (45-minute interview)

- **Clarification**: 5 min
- **Design discussion**: 5 min
- **Basic implementation**: 10 min
- **Tie-breaking**: 5 min
- **Testing**: 5 min
- **Weighted extension**: 10 min
- **Scale discussion**: 5 min

---

## Related Practice Problems

**LeetCode:**
- 347: Top K Frequent Elements
- 692: Top K Frequent Words
- 973: K Closest Points to Origin
- 355: Design Twitter (ranking timeline)

**System Design:**
- Design Yelp (business ratings)
- Design Uber (driver ratings)
- Design a leaderboard system
- Design a recommendation system

---

## Atlassian-Specific Context

**Why this question?**
- Atlassian builds tools like Jira Service Management
- Real problem: ranking support agents by performance
- Tests: OOP, algorithms, system design, production thinking

**What they're looking for:**
- **Collaboration**: Ask questions, discuss trade-offs
- **Quality**: Write production-grade code
- **Scale**: Think about their product scale (millions of users)
- **Customer focus**: How does this improve customer experience?

---

## Quick Reference: Sorting with Tie-Breaking

```python
# Single criteria
sorted(agents, key=lambda a: -a.get_average_rating())

# Tie-break by agent_id
sorted(agents, key=lambda a: (-a.get_average_rating(), a.agent_id))

# Multiple tie-breaks
sorted(agents, key=lambda a: (
    -a.get_average_rating(),    # Primary: higher avg first
    -len(a.ratings),            # Secondary: more ratings first
    a.agent_id                  # Tertiary: lower ID first
))

# Using tuple comparison (clean and Pythonic)
def sort_key(agent):
    return (-agent.get_average_rating(), agent.agent_id)

sorted(agents, key=sort_key)
```

---

## Practice Scenario

**You have 15 minutes. Implement:**
1. Agent class with rating validation
2. System class with record_rating and get_average_rating
3. Sorting by average with agent_id tie-breaking
4. Extension for weighted ratings

**Then discuss:**
- How to scale to 1M agents?
- How to handle real-time updates?
- How to add time-decay weights?

Good luck! 🚀
