# Atlassian Principal Backend Engineer Interview Prep

Complete preparation package for Atlassian's coding interviews, specifically for **Principal Backend Engineer** role.

## 📚 What's Included

This repository contains solutions, tests, and detailed guides for the two most commonly asked Atlassian coding questions:

### Problem 1: Vote Counter ⚡
Given a list of votes, find the winner.
- **Difficulty:** Easy (warm-up question)
- **Time:** 15-20 minutes
- **Concepts:** Hash maps, counting, optimization

### Problem 2: Agent Rating System 🎯
Design a system to track and rank support agents by their ratings.
- **Difficulty:** Medium (main question)
- **Time:** 30-35 minutes
- **Concepts:** OOP, sorting, tie-breaking, weighted averages

---

## 🚀 Quick Start

### 1. Run the Demos
See both problems in action:
```bash
python demo_all.py
```

### 2. Run the Tests
Verify all implementations:
```bash
# Install pytest if needed
pip install pytest

# Run all tests
python -m pytest src/test_vote_counter.py -v
python -m pytest src/test_agent_rating_system.py -v
```

### 3. Practice with Timer
Simulate interview conditions:
```bash
python src/practice_session.py
```

---

## 📁 File Structure

```
prep/
│
├── README.md                              ← You are here
├── ATLASSIAN_PROBLEMS_SUMMARY.md          ← Overview of both problems
├── demo_all.py                            ← Interactive demos
│
├── ATLASSIAN_INTERVIEW_PREP.md            ← Problem 1: Vote Counter guide
├── AGENT_RATING_INTERVIEW_PREP.md         ← Problem 2: Agent Rating guide
│
└── src/
    ├── vote_counter.py                    ← Problem 1: 6 implementations
    ├── test_vote_counter.py               ← Problem 1: Test suite
    │
    ├── agent_rating_system.py             ← Problem 2: Multiple implementations
    ├── test_agent_rating_system.py        ← Problem 2: Test suite
    │
    └── practice_session.py                ← Timed practice tool
```

---

## 📖 Study Guide

### Phase 1: Understanding (Day 1 - 2-3 hours)

1. **Read the overview**
   ```bash
   # Open in your editor
   ATLASSIAN_PROBLEMS_SUMMARY.md
   ```

2. **Run the demos**
   ```bash
   python demo_all.py
   ```
   Choose option 6 to run all demos.

3. **Study the implementations**
   - [src/vote_counter.py](src/vote_counter.py) - Read all 6 approaches
   - [src/agent_rating_system.py](src/agent_rating_system.py) - Understand the OOP design

4. **Read the interview guides**
   - [ATLASSIAN_INTERVIEW_PREP.md](ATLASSIAN_INTERVIEW_PREP.md)
   - [AGENT_RATING_INTERVIEW_PREP.md](AGENT_RATING_INTERVIEW_PREP.md)

### Phase 2: Practice Coding (Day 2-3 - 2-3 hours)

1. **Vote Counter** - Code from scratch 3 times
   - Target: Complete in < 15 minutes
   - Include: Basic solution + tie detection
   - Test with: Example, edge cases, ties

2. **Agent Rating System** - Code from scratch 2 times
   - Target: Basic version in < 20 minutes
   - Include: Agent class + System class + sorting
   - Test with: Multiple agents, tie scenarios

3. **Weighted Extension** - Add weighted ratings
   - Target: 10 minutes to extend basic solution
   - Include: WeightedAgentRatingSystem class

### Phase 3: Advanced Topics (Day 4 - 2 hours)

1. **Study follow-up questions** in both guides
   - How to scale to 1B records?
   - Real-time processing approaches
   - Redis leaderboard implementation
   - Time-decay weighted systems

2. **Practice explaining your approach**
   - Record yourself or practice with a friend
   - Focus on clear communication
   - Explain trade-offs

### Phase 4: Mock Interviews (Day 5 - 2 hours)

1. **Timed practice sessions**
   ```bash
   python src/practice_session.py
   ```

2. **Self-review checklist**
   - Did you ask clarifying questions?
   - Did you explain your approach first?
   - Did you test your code?
   - Did you discuss complexity?

### Phase 5: Final Review (Day 6 - 1 hour)

1. Review the cheat sheets in [ATLASSIAN_PROBLEMS_SUMMARY.md](ATLASSIAN_PROBLEMS_SUMMARY.md)
2. Review common mistakes section in both guides
3. Practice clarifying questions
4. Rest and prepare mentally

---

## 🎯 Interview Strategy

### Before You Code
1. **Listen carefully** to the problem statement
2. **Ask clarifying questions**:
   - Vote Counter: "How should we handle ties?"
   - Agent Rating: "What tie-breaking strategy should we use?"
3. **Explain your approach** before coding
4. **Confirm understanding** with the interviewer

### While Coding
1. **Think out loud** - explain what you're doing
2. **Write clean code** - use meaningful names, type hints
3. **Validate inputs** - check for edge cases
4. **Test as you go** - don't wait until the end

### After Coding
1. **Walk through test cases**:
   - Example from problem
   - Edge cases (empty, single element)
   - Tie scenarios
2. **Analyze complexity**: Time and space
3. **Discuss extensions**: How to scale, optimize, extend

---

## 💡 Key Success Factors for Principal Role

### 1. System Design Thinking (Critical!)
Don't just solve the algorithm - think about production:
- "How would this scale to 1M agents?"
- "What if we need real-time updates?"
- "How would we monitor this in production?"

### 2. Code Quality
- Type hints on all functions
- Input validation
- Clean variable names
- Proper error handling
- Docstrings

### 3. Communication
- Ask questions before coding
- Explain trade-offs
- Think out loud
- Take feedback gracefully

### 4. Testing Mindset
- Walk through test cases
- Consider edge cases proactively
- Mention how you'd write unit tests

---

## 🎓 What Atlassian Looks For

**Atlassian Values:** Open company, no bullshit, build with heart and balance, don't #@!% the customer, play as a team

**In Practice:**
- ✅ Ask clarifying questions (collaboration)
- ✅ Write production-quality code (craftsmanship)
- ✅ Think about customer impact (customer-centric)
- ✅ Discuss monitoring and observability (reliability)
- ✅ Show how you think, not just what you know (transparency)

---

## 📊 Complexity Quick Reference

### Vote Counter
- **Time:** O(n) where n = number of votes
- **Space:** O(k) where k = unique candidates
- **Optimal:** Yes - must see every vote

### Agent Rating System
- **record_rating():** O(1)
- **get_average():** O(1) or O(m) if recomputed
- **get_sorted_agents():** O(n log n) where n = agents
- **get_top_k():** O(n log k) with heap optimization

---

## 🔗 Additional Resources

### LeetCode Practice Problems
- [347: Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/)
- [692: Top K Frequent Words](https://leetcode.com/problems/top-k-frequent-words/)
- [355: Design Twitter](https://leetcode.com/problems/design-twitter/)

### System Design Topics
- Redis Sorted Sets (leaderboards)
- Time-series databases
- Stream processing (Kafka)
- Caching strategies (Redis, Memcached)

### Atlassian Interview Reports
- [Glassdoor - Atlassian](https://www.glassdoor.com/Interview/Atlassian-Interview-Questions-E115699.htm)
- Search "Atlassian Principal Backend Engineer interview" on Blind
- LeetCode Discuss - Atlassian tag

---

## ✅ Pre-Interview Checklist

Day before interview:
- [ ] Can code Vote Counter in < 15 minutes
- [ ] Can code Agent Rating System basic in < 20 minutes
- [ ] Can extend with weighted ratings in < 10 minutes
- [ ] Can explain O(n) vs O(n log n) complexity
- [ ] Know how to use Redis for leaderboards
- [ ] Can discuss 1B scale approach
- [ ] Practiced clarifying questions
- [ ] Reviewed Atlassian values

Day of interview:
- [ ] Review cheat sheets (see ATLASSIAN_PROBLEMS_SUMMARY.md)
- [ ] Review common follow-ups
- [ ] Test your coding environment
- [ ] Prepare questions to ask interviewer
- [ ] Relax and breathe!

---

## 🆘 Common Mistakes to Avoid

### Vote Counter
❌ Using O(n log n) sort instead of O(n) hash map
❌ Not handling empty input
❌ Forgetting to discuss tie-breaking

### Agent Rating System
❌ Not using OOP (just functions)
❌ Hardcoding tie-breaking logic
❌ Forgetting input validation (rating must be 1-5)
❌ Not testing edge cases

### Both Problems
❌ Jumping into code without clarifying
❌ Not explaining your approach first
❌ Not testing your code
❌ Missing complexity analysis
❌ Being defensive when given feedback

---

## 💬 Sample Opening (Use This!)

> "Let me make sure I understand the problem correctly. [Restate problem]
>
> Before I start, I have a few clarifying questions:
> - [Question about edge cases]
> - [Question about requirements]
> - [Question about scale/constraints]
>
> Great, so my approach will be [explain approach]. This will be O(n) time
> and O(k) space. Does that sound good?
>
> Alright, let me start coding..."

---

## 🎮 Quick Commands Reference

```bash
# Run interactive demos
python demo_all.py

# Run all demos at once (non-interactive)
python demo_all.py --all

# Run timed practice
python src/practice_session.py

# Run tests
python -m pytest src/test_vote_counter.py -v
python -m pytest src/test_agent_rating_system.py -v

# Run specific test
python -m pytest src/test_vote_counter.py::TestBasicFunctionality -v

# Run with coverage (optional)
pip install pytest-cov
python -m pytest src/ --cov=src --cov-report=html
```

---

## 🎯 Interview Day Tips

### 30 Minutes Before
1. Review cheat sheets in ATLASSIAN_PROBLEMS_SUMMARY.md
2. Review your clarifying questions list
3. Do a quick stretch / breathing exercise
4. Test your microphone and screen sharing

### During Interview
1. **Listen actively** - take notes if needed
2. **Ask questions** - clarify before coding
3. **Think out loud** - show your thought process
4. **Stay calm** - if stuck, explain what you're thinking
5. **Accept hints** - interviewers want you to succeed
6. **Communicate** - tell them if you need a moment to think

### After Coding
1. **Test thoroughly** - walk through multiple cases
2. **Explain complexity** - time and space
3. **Discuss trade-offs** - when asked about extensions
4. **Ask questions** - about the team, tech stack, culture

---

## 🏆 Success Stories Pattern

Most successful candidates:
1. Started by asking 3-5 clarifying questions
2. Explained their approach before coding
3. Wrote clean, well-structured code with type hints
4. Tested their code thoroughly
5. Discussed complexity and trade-offs
6. Extended the solution when asked
7. Showed enthusiasm and collaboration

---

## 📞 Support

If you find issues or have questions:
- Review the detailed guides in the markdown files
- Run the demos to see working examples
- Check the test files for edge cases
- Practice explaining out loud

---

## 🎓 Good Luck!

You've got a comprehensive prep package:
- ✅ Working implementations
- ✅ Comprehensive tests
- ✅ Detailed interview guides
- ✅ Interactive practice tools
- ✅ Common follow-ups with answers

**Remember:** Atlassian wants to see how you think, communicate, and collaborate.
Show them you can write clean code, explain your decisions, and think about
production concerns. You've got this! 🚀

---

**Final Tip:** The night before your interview, don't cram. Review the cheat
sheets, get good sleep, and trust your preparation. You're ready!
