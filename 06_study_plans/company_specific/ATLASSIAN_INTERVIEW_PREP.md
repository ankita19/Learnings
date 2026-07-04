# Atlassian Principal Backend Engineer - Vote Counter Prep

## Problem Statement
Given a list of votes for candidates, determine the winner based on the total number of votes.

**Example**: `['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']`

---

## Interview Approach (5-Step Framework)

### 1. **Clarify Requirements** (2-3 minutes)
Ask these questions to show senior-level thinking:

- **Tie handling**: What happens if multiple candidates have the same max votes?
  - Return all winners?
  - Return the first one encountered?
  - Return None/error?

- **Input validation**:
  - Can the votes list be empty?
  - Can it contain None or invalid values?
  - Are candidate IDs always strings?

- **Scale**:
  - How many votes (N)?
  - How many unique candidates (K)?
  - Is this real-time or batch processing?

- **Output format**:
  - Just the winner's name?
  - Include vote count?
  - Need full breakdown?

### 2. **Discuss Approach** (2 minutes)

**Optimal Solution**:
```
1. Use a hash map (dict) to count votes: O(n) time, O(k) space
2. Find candidate with max count: O(k) time
3. Total: O(n + k) ≈ O(n) since k ≤ n
```

**Why this is optimal**:
- Single pass through data
- Minimal space (only unique candidates)
- Cannot do better than O(n) - must see every vote

### 3. **Code the Solution** (10-15 minutes)

Start with the **cleanest Pythonic solution**:

```python
from collections import Counter

def find_winner(votes: List[str]) -> Optional[str]:
    if not votes:
        return None
    return Counter(votes).most_common(1)[0][0]
```

**Then enhance based on discussion**:
- Add tie detection if required
- Add input validation if mentioned
- Add detailed results if needed

### 4. **Test Your Code** (3-5 minutes)

Walk through test cases:
- **Happy path**: Clear winner
- **Edge cases**: Empty, single vote, all same
- **Ties**: Two-way, three-way ties
- **Invalid input**: None, empty strings

### 5. **Discuss Trade-offs & Extensions** (5 minutes)

See "Follow-up Questions" section below.

---

## Key Points for Principal Engineer Level

### What Sets You Apart:

1. **Clarification Before Coding**
   - Don't jump straight into code
   - Ask about edge cases and requirements
   - Show product thinking, not just coding

2. **Production-Ready Mindset**
   - Type hints
   - Docstrings
   - Error handling
   - Logging considerations

3. **Testing Strategy**
   - Unit tests for functionality
   - Edge case coverage
   - Performance tests for scale

4. **System Design Thinking**
   - What if this was 1B votes?
   - Real-time vs batch?
   - Distributed counting?

5. **Communication**
   - Explain your thought process
   - Discuss trade-offs
   - Ask for feedback

---

## Common Follow-up Questions

### Q1: "What if we have 1 billion votes?"

**Answer approach**:
- Single machine: Stream processing, still O(n) but memory-efficient
- Distributed: MapReduce pattern
  - Map: Partition votes, count locally
  - Reduce: Aggregate counts
- Database: Use GROUP BY with COUNT
- Consider: Approximate algorithms (Count-Min Sketch) if exact count not needed

```python
# Streaming approach for memory efficiency
def find_winner_streaming_large_file(file_path: str):
    vote_counts = {}
    with open(file_path, 'r') as f:
        for line in f:
            vote = line.strip()
            vote_counts[vote] = vote_counts.get(vote, 0) + 1
    return max(vote_counts, key=vote_counts.get)
```

### Q2: "What if votes are coming in real-time?"

**Answer approach**:
- Maintain running counts in memory/Redis
- Update winner incrementally
- Consider: Winner might change as votes come in
- Trade-off: Slightly more work per vote vs full recount

```python
class RealtimeVoteCounter:
    def __init__(self):
        self.counts = {}
        self.current_winner = None
        self.max_votes = 0

    def add_vote(self, candidate: str):
        self.counts[candidate] = self.counts.get(candidate, 0) + 1
        if self.counts[candidate] > self.max_votes:
            self.max_votes = self.counts[candidate]
            self.current_winner = candidate

    def get_winner(self):
        return self.current_winner
```

### Q3: "What if we need to prevent fraud/duplicate votes?"

**Answer approach**:
- Need voter identification
- Change data structure: `dict[voter_id] = candidate`
- Validate: One vote per voter
- Consider: Time windows, IP tracking, authentication

### Q4: "How would you scale this horizontally?"

**Answer approach**:
```
1. Partition votes across multiple workers (by hash of candidate ID)
2. Each worker maintains partial counts
3. Coordinator aggregates and finds global max
4. Use: Apache Kafka, Redis Streams, etc.
```

### Q5: "What if we need historical trending?"

**Answer approach**:
- Store votes with timestamps
- Time-series database (InfluxDB, TimescaleDB)
- Aggregation at different granularities
- Caching strategy for frequently queried periods

### Q6: "What are the space/time complexities?"

**Answer**:
- **Time**: O(n) where n = number of votes (must see each vote once)
- **Space**: O(k) where k = unique candidates (worst case: O(n) if all unique)
- **Cannot do better** than O(n) time - must count every vote

### Q7: "What if memory is limited?"

**Answer approaches**:
1. **External sorting**: Sort votes, then sequential count
2. **Streaming with spill to disk**: Keep top K in memory
3. **Approximate**: HyperLogLog for cardinality, Count-Min Sketch for frequencies
4. **Database**: Let DB handle with proper indexing

---

## Red Flags to Avoid

❌ **Don't**:
- Jump into coding without clarifying
- Ignore edge cases
- Write bugs in basic scenarios
- Miss the O(n) solution (suggesting sort O(n log n))
- Forget to test your code
- Write sloppy, unreadable code

✅ **Do**:
- Ask clarifying questions
- Explain your approach before coding
- Write clean, readable code
- Add type hints for Python
- Test edge cases
- Discuss trade-offs
- Show system design thinking

---

## Atlassian-Specific Tips

1. **Culture Fit**: Atlassian values collaboration
   - Ask for feedback during interview
   - Be open to suggestions
   - Explain your thinking clearly

2. **Focus on Quality**: They value craftsmanship
   - Write production-quality code
   - Think about maintainability
   - Consider the team that will maintain this

3. **Customer-Centric**: Think about end users
   - Why does accuracy matter?
   - What happens if it's wrong?
   - How would you monitor this in production?

4. **Scale**: Atlassian products have massive scale
   - Always discuss scalability
   - Think distributed systems
   - Consider observability

---

## Practice Run Script

### Opening (30 seconds):
"Let me make sure I understand the problem. We have a list of votes, and we need to find which candidate received the most votes. A few clarifying questions..."

### Clarification (1-2 minutes):
- "What should we return if there's a tie?"
- "Can the input be empty?"
- "What's the expected scale - thousands or millions of votes?"
- "Do we need just the winner or full vote breakdown?"

### Approach (1 minute):
"I'll use a hash map to count votes in a single pass - O(n) time complexity. Then find the max count - O(k) for unique candidates. This is optimal since we must examine every vote."

### Coding (10 minutes):
Write clean solution with Counter, then enhance based on requirements.

### Testing (3 minutes):
"Let me test with: [example from problem], empty list, tie scenario..."

### Discussion (5 minutes):
Be ready for scale/system design questions.

---

## Time Allocation (45-min interview)

- Intros: 5 min
- Problem + Clarification: 5 min
- Coding: 15-20 min
- Testing: 5 min
- Follow-ups: 10-15 min

---

## Additional Resources

**Practice more**:
- Top K Frequent Elements (LeetCode 347)
- Group Anagrams (LeetCode 49)
- First Unique Character (LeetCode 387)

**System Design**:
- Design a polling system
- Design Twitter trending topics
- Design leaderboard system

**Atlassian Interview Reports**:
- Glassdoor reviews
- Blind discussions
- leetcode.com/discuss

Good luck! 🚀
