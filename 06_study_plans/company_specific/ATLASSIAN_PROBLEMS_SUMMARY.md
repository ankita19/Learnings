# Atlassian Principal Backend Engineer - Problem Summary

Two commonly asked coding questions at Atlassian interviews:

---

## Problem 1: Vote Counter

**Difficulty:** Easy (Warm-up)
**Time:** 15-20 minutes
**Focus:** Hash maps, counting, optimization

### Problem
Given a list of votes for candidates, determine the winner.

**Example:** `['c1', 'c2', 'c1', 'c2', 'c1', 'c2', 'c3', 'c4', 'c4']`

### Key Points
- Use Counter/HashMap: O(n) time, O(k) space
- Handle ties appropriately
- Discuss scalability (1B votes, real-time)

### Files
- [vote_counter.py](src/vote_counter.py) - 6 implementations
- [test_vote_counter.py](src/test_vote_counter.py) - Comprehensive tests
- [ATLASSIAN_INTERVIEW_PREP.md](ATLASSIAN_INTERVIEW_PREP.md) - Full guide

---

## Problem 2: Agent Rating System

**Difficulty:** Medium (Main Question)
**Time:** 30-35 minutes
**Focus:** OOP, design patterns, sorting, extensions

### Problem
Design a system for support agent ratings:
- Agents receive ratings (1-5)
- Compute average ratings
- Sort agents by rating
- Handle tie-breaking
- **Extension:** Weighted votes

### Key Points
- Use OOP (Agent class + System class)
- Multiple tie-breaking strategies (enum pattern)
- Sorting with custom comparators
- Weighted average for extension
- Discuss: Redis leaderboard, time-decay, outliers

### Files
- [agent_rating_system.py](src/agent_rating_system.py) - Multiple implementations
- [test_agent_rating_system.py](src/test_agent_rating_system.py) - Full test suite
- [AGENT_RATING_INTERVIEW_PREP.md](AGENT_RATING_INTERVIEW_PREP.md) - Detailed guide

---

## Comparison

| Aspect | Vote Counter | Agent Rating System |
|--------|--------------|---------------------|
| **Complexity** | Easy | Medium |
| **Time** | 15-20 min | 30-35 min |
| **Data Structure** | HashMap | Classes + HashMap |
| **Algorithm** | Counting | Counting + Sorting |
| **OOP** | Optional | Required |
| **Extensions** | Scale, real-time | Weights, tie-breaking |
| **Interview Stage** | First question / warm-up | Main coding question |

---

## Typical Interview Flow

### 45-Minute Technical Interview:

**Option A: Single Problem**
- 5 min: Intros
- 35 min: Agent Rating System (with weighted extension)
- 5 min: Questions

**Option B: Two Problems**
- 5 min: Intros
- 15 min: Vote Counter
- 25 min: Agent Rating System (basic + one extension)
- 5 min: Questions

**Option C: Problem + System Design**
- 5 min: Intros
- 20 min: Agent Rating System (coding)
- 15 min: Scale to production (system design)
- 5 min: Questions

---

## Study Plan

### Day 1: Foundations (2-3 hours)
1. Read both problem guides
2. Study the provided implementations
3. Run the code and tests
4. Understand time/space complexity

### Day 2: Practice Coding (2-3 hours)
1. Code Vote Counter from scratch (3 times)
2. Code Agent Rating System basic version (2 times)
3. Add weighted extension (2 times)
4. Time yourself

### Day 3: Advanced Topics (2 hours)
1. Study follow-up questions
2. Practice explaining scale solutions
3. Review system design patterns
4. Practice Redis leaderboard approach

### Day 4: Mock Interviews (2 hours)
1. Use [practice_session.py](src/practice_session.py)
2. Record yourself explaining
3. Practice whiteboarding
4. Review common mistakes

### Day 5: Polish (1 hour)
1. Review both prep guides
2. Practice opening/clarifying questions
3. Review Atlassian values and culture
4. Rest and prepare mentally

---

## Common Follow-ups (Both Problems)

### Scalability
- **1 billion records?** → Database, sharding, caching
- **High write throughput?** → Kafka, stream processing
- **Low latency reads?** → Redis, materialized views

### Distributed Systems
- **Multiple servers?** → Partitioning, coordination
- **Consistency?** → Event sourcing, CRDT
- **Fault tolerance?** → Replication, checkpointing

### Advanced Features
- **Fraud prevention?** → Deduplication, rate limiting
- **Historical trends?** → Time-series DB
- **Real-time updates?** → WebSockets, Redis Pub/Sub

---

## Key Success Factors for Principal Role

### 1. Communication (30%)
- Ask clarifying questions before coding
- Explain your thought process
- Discuss trade-offs openly
- Take feedback gracefully

### 2. Problem Solving (30%)
- Start with simple solution
- Optimize iteratively
- Consider edge cases
- Test thoroughly

### 3. Code Quality (20%)
- Clean, readable code
- Type hints and validation
- Meaningful names
- Proper abstractions

### 4. System Thinking (20%)
- Consider scale from start
- Think about production
- Discuss monitoring/observability
- Know when to use what technology

---

## Red Flags That Fail Interviews

❌ **Avoid These:**
1. Jumping into code without clarifying
2. Ignoring edge cases
3. Writing buggy code in simple scenarios
4. Unable to explain complexity
5. Defensive when given feedback
6. Not testing your code
7. Missing obvious optimizations
8. Over-engineering simple problems
9. Under-engineering complex problems
10. Poor communication

---

## Atlassian Culture Fit

**Values:** Open company, no bullshit, build with heart and balance, don't #@!% the customer, play as a team

**What this means in interviews:**
- **Be honest** - Say "I don't know" when you don't
- **Collaborate** - Ask for hints, discuss approaches
- **Customer focus** - Think about end users
- **Quality** - Write code you'd be proud to ship
- **Teamwork** - Show you can work with others

---

## Quick Reference Cards

### Vote Counter Cheat Sheet
```python
from collections import Counter

def find_winner(votes):
    if not votes:
        return None
    return Counter(votes).most_common(1)[0][0]

# Complexity: O(n) time, O(k) space
# Follow-ups: Scale, real-time, fraud prevention
```

### Agent Rating Cheat Sheet
```python
class Agent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.ratings = []

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average(self):
        return sum(self.ratings) / len(self.ratings)

class System:
    def __init__(self):
        self.agents = {}

    def record(self, agent_id, rating):
        if agent_id not in self.agents:
            self.agents[agent_id] = Agent(agent_id)
        self.agents[agent_id].add_rating(rating)

    def get_sorted(self):
        return sorted(self.agents.values(),
                     key=lambda a: (-a.get_average(), a.agent_id))

# Complexity: O(n log n) sorting
# Follow-ups: Weights, tie-breaking, Redis leaderboard
```

---

## Resources

### LeetCode Practice
- [347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
- [355: Design Twitter](https://leetcode.com/problems/design-twitter/)

### System Design
- Redis Sorted Sets (leaderboards)
- Time-series databases
- Stream processing (Kafka)
- Caching strategies

### Atlassian Interview Reports
- Glassdoor: Filter for "Principal Backend Engineer"
- Blind: Search "Atlassian interview"
- LeetCode Discuss: Atlassian tag

---

## Final Checklist

Before your interview, ensure you can:

**Vote Counter:**
- [ ] Implement in < 15 minutes
- [ ] Handle ties properly
- [ ] Explain O(n) complexity
- [ ] Discuss 1B scale solution

**Agent Rating System:**
- [ ] Implement basic version in < 20 minutes
- [ ] Add tie-breaking strategy
- [ ] Extend with weighted votes
- [ ] Explain Redis leaderboard approach

**Soft Skills:**
- [ ] Ask 3-5 clarifying questions
- [ ] Explain approach before coding
- [ ] Test with multiple test cases
- [ ] Discuss trade-offs confidently
- [ ] Handle follow-ups gracefully

---

## On Interview Day

### Pre-Interview (30 min before)
- Review both cheat sheets above
- Review common follow-ups
- Practice clarifying questions
- Relax and breathe

### During Interview
- Listen carefully to the problem
- Ask clarifying questions
- Think out loud
- Write clean code
- Test thoroughly
- Be honest about what you don't know

### Post-Interview
- Send thank you email
- Note what went well/poorly
- Don't stress - you prepared well!

---

Good luck! You've got this! 🚀

**Remember:** Atlassian values how you think and communicate as much as your coding ability. Show them you can collaborate, explain your thinking, and build quality software.
