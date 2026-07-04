# Interview Prep Plan — 14 Days, 1.5 hrs/day

## Context
- Target: Capital One technical interviews (Arrays/Hashing, Two-pointer, Sliding Window, Trees/Graphs)
- Time available: 1 – 1.5 hours/day
- Language: Python
- Tool: NeetCode (lifetime subscription)

---

## Daily Structure (every single day)

| Block | Time | What |
|---|---|---|
| Cold recall | 15 min | Rewrite yesterday's solution from scratch, no reference |
| Deep solve | 50 min | Today's problem — speak approach first, then code |
| Transfer drill | 20 min | 1 variation — pseudocode it in 10 min |
| Pattern log | 5 min | Write the pattern in your own words |

> **Rule:** Cold recall is first. Always. Skip it and the plan fails.

---

## Java → Python Syntax Map

Your brain defaults to Java. Use this table until Python feels natural.

| Java | Python |
|---|---|
| `int[] arr = new int[26]` | `arr = [0] * 26` |
| `int[] arr = new int[n]` | `arr = [0] * n` |
| `HashMap<Integer,Integer> map = new HashMap<>()` | `map = {}` |
| `map.containsKey(x)` | `x in map` |
| `map.getOrDefault(x, 0)` | `map.get(x, 0)` |
| `map.put(x, map.getOrDefault(x,0) + 1)` | `map[x] = map.get(x, 0) + 1` |
| `for (int i = 0; i < n; i++)` | `for i in range(n):` |
| `for (int x : arr)` | `for x in arr:` |
| `arr.length` | `len(arr)` |
| `s.charAt(i)` | `s[i]` |
| `s.length()` | `len(s)` |
| `Collections.sort(arr)` | `arr.sort()` |
| `new PriorityQueue<>()` + `heap.offer(x)` + `heap.poll()` | `heap = []` + `heapq.heappush(heap, x)` + `heapq.heappop(heap)` |
| `heap.peek()` | `heap[0]` |
| iterating map keys: `for (int k : map.keySet())` | `for k in count:` — no `.keys()` needed |

> **Common Java leak to watch:** No `[]` after variable name on the left side. `counter[] = ...` is Java. `counter = [0] * 26` is Python.

> **Key mental shift:** In Java, heap is an object with methods. In Python, heap is just a plain list — `heapq` is a module that operates on it from outside. Always min-heap. To simulate max-heap, negate the value: `heapq.heappush(heap, -value)`.

---

## Phase 1 — Days 1–3: Python Fluency

Fix syntax before touching algorithms. Syntax breaking mid-problem is your #1 blocker.

### Day 1 — Dictionary Operations
Write each of these 10 times from scratch. No autocomplete.

```python
d = {}
d[key] = value
key in d
d.get(key, default)
for k, v in d.items():
from collections import defaultdict, Counter
```

### Day 2 — Iteration Patterns
Write each until automatic.

```python
for i, val in enumerate(arr):
sorted(arr, key=lambda x: x[1])
[x for x in arr if x > 0]
arr[::-1]
arr[i:j]
```

### Day 3 — Standard Library
Drill until these feel natural.

```python
from collections import deque
q = deque()
q.append(x)
q.popleft()

import heapq
heapq.heappush(h, val)
heapq.heappop(h)

from collections import Counter
Counter("aabbc")   # know what it returns
```

---

## Phase 2 — Days 4–11: 4 Patterns (2 Days Each)

**Day A:** Understand pattern deeply, solve 1 base problem
**Day B:** Solve 2 variations cold (never seen before)

---

### Pattern 1 — HashMap Lookup (Days 4–5)

**Core insight:** Store what you've SEEN, check what you NEED

#### Day 4 — Two Sum
- Solve one-pass using a seen dict
- After solving: explain in one sentence why one-pass is better than two-pass

#### Day 5 — Group Anagrams
- Same pattern, different shape: store → compare → group
- Transfer Q: "What if strings can have unicode characters?"

---

### Pattern 2 — Two Pointers (Days 6–7)

**Core insight:** Left and right converge — compare and move based on a condition

#### Day 6 — Valid Palindrome
- After solving: state the invariant you maintain at every step

#### Day 7 — Container With Most Water
- Same two pointers, now maximizing an area
- Transfer Q: "What if the array has negative heights?"

---

### Pattern 3 — Sliding Window (Days 8–9)

**Core insight:** Expand right, shrink left when constraint breaks

**Before coding — answer these 3 questions first (write as comments):**
```
Q1. What is my state?          e.g. window = {}  or  window_sum = 0
Q2. When is window invalid?    e.g. len(window) > k  or  window_sum > k
Q3. How do I remove left?      e.g. window[c] -= 1, del if 0
```

**Template to memorize — one pattern for ALL variants:**
```python
left = 0
window = {}       # Q1: always a dict (count) — same structure every time
result = 0

for right, char in enumerate(s):
    window[char] = window.get(char, 0) + 1    # expand

    while INVALID:        # Q2: condition changes per problem
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1         # Q3: always same removal pattern

    result = max(result, right - left + 1)

return result
```

**Only the `while` condition changes across variants:**
| Variant | `while` condition |
|---|---|
| No repeats | `window[char] > 1` |
| ≤ K distinct | `len(window) > k` |
| Sum ≤ K | `window_sum > k` (use int, not dict) |

> **Key insight:** No-repeats uses the same dict + same removal pattern as ≤ K distinct. Only the condition differs. Do NOT use the "jump left" shortcut in interviews — it's a different structure that's harder to recall under pressure.

#### Day 8 — Longest Substring Without Repeating Characters
- Memorize and internalize the template above

#### Day 9 — Minimum Window Substring
- Same template, harder constraint
- Transfer Q: "What if you need the longest valid window instead of minimum?"

---

### Pattern 4 — Trees BFS / DFS (Days 10–11)

Capital One explicitly lists trees/graphs. Most senior engineers lose marks here.

**BFS Template:**
```python
from collections import deque
q = deque([root])
while q:
    for _ in range(len(q)):   # this loop = one level
        node = q.popleft()
        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
```

#### Day 10 — Binary Tree Level Order Traversal
- Internalize the BFS template above

#### Day 11 — Number of Islands
- Same BFS idea applied to a grid
- Transfer Q: "What if diagonal connections also count as land?"

---

## Phase 3 — Days 12–14: Retrieval + Simulation

### Day 12 — Pattern Identification Drill
- Given 5 problem descriptions (no code)
- Your only job: name the pattern + state the invariant
- No coding. Pure recognition training.

### Day 13 — Timed Mock
- 2 problems back to back, 60 minutes total
- Rules: no googling, no autocomplete, speak your approach before typing
- After: note the exact line/moment you slowed down or got stuck

### Day 14 — Confidence Consolidation
- Write all 4 pattern templates from memory
- Solve 1 easy problem cleanly — no bugs, good variable names
- **Stop. No new problems.** You need to feel ready, not cramped.

---

## Your Pattern Templates (fill these in as you learn each one)

### HashMap
```python
# Two Sum pattern
seen = {}
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Two Pointers
```python
left, right = 0, len(arr) - 1
while left < right:
    # compare or compute
    if condition:
        left += 1
    else:
        right -= 1
```

### Sliding Window
```python
# Before coding: answer Q1 / Q2 / Q3 as comments
# Q1: state?   Q2: invalid when?   Q3: remove left how?

left = 0
window = {}       # always a dict — same structure every time
result = 0

for right, char in enumerate(s):
    window[char] = window.get(char, 0) + 1

    while INVALID:                    # Q2 — only line that changes
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1

    result = max(result, right - left + 1)

# Conditions: no repeats → window[char]>1 | ≤K distinct → len(window)>k | sum≤K → window_sum>k (int not dict)
```

### BFS (Tree / Grid)
```python
from collections import deque
q = deque([start])
visited = set([start])
while q:
    node = q.popleft()
    for neighbor in get_neighbors(node):
        if neighbor not in visited:
            visited.add(neighbor)
            q.append(neighbor)
```

---

## Weak Areas & Key Learnings

> Add to this section every time you get stuck or learn something non-obvious. Review before every session.

---

### 1. Bucket Sort Initialization — Top K Frequent Elements

**What tripped you:** Could not recall `freq = [[] for _ in range(len(nums) + 1)]`

**Mental model — ask 3 questions, don't memorize:**
```
Q1: What am I indexing by?            → frequency count
Q2: What's the max possible frequency? → len(nums)  (all elements same)
Q3: How many buckets do I need?        → len(nums) + 1  (index 0 to len(nums))
```

**Result:**
```python
freq = [[] for _ in range(len(nums) + 1)]
# Just len(nums)+1 empty lists. Nothing more.
# freq[3] will hold all numbers that appear exactly 3 times.
```

**Java equivalent (3 lines vs 1):**
```java
List<Integer>[] freq = new ArrayList[nums.length + 1];
for (int i = 0; i < freq.length; i++) {
    freq[i] = new ArrayList<>();
}
```

---

### 2. Iterating Backwards — Prefer `reversed()` over `range`

**What tripped you:** `for i in range(len(freq) - 1, 0, -1)` felt unreadable

**Cleaner Python way:**
```python
for bucket in reversed(freq):   # reads right to left, no index needed
    for num in bucket:
        ...
```

**When range version is needed:** only if you need the index `i` inside the loop.

**Java equivalent:**
```java
for (int i = freq.length - 1; i > 0; i--)
```

---

### 3. Frequency Counting Pattern

**Standard form — always write it this way:**
```python
count = {}
for num in nums:
    count[num] = count.get(num, 0) + 1
```

**Why `get(num, 0) + 1` not `1 + get(num, 0)`:** reads left to right — "get current, add 1". Easier to reconstruct under pressure.

---

### 5. heapq — Heap in Python

**What tripped you:** heapq syntax feels alien coming from Java

**The only 4 lines you need:**
```python
import heapq

heap = []                          # just a plain list
heapq.heappush(heap, value)        # push
heapq.heappop(heap)                # pop smallest (always min-heap)
heap[0]                            # peek without removing
```

**Tuple push (for Top K):**
```python
heapq.heappush(heap, (count[num], num))  # sorts by first element (count)
heapq.heappop(heap)[1]                   # pop and get the number, not the count
```

**Max-heap:** negate the value
```python
heapq.heappush(heap, -value)
-heapq.heappop(heap)   # negate again to get original
```

**Java equivalent:**
```java
PriorityQueue<int[]> heap = new PriorityQueue<>((a, b) -> a[0] - b[0]);
heap.offer(new int[]{count.get(num), num});
heap.poll();
heap.peek();
```

---

### 4. Java Syntax Leaking Into Python

**What tripped you:** Writing `counter[] = [0]*26` (Java array declaration leak)

**Rule:** `[]` never appears on the LEFT side of assignment in Python.
```python
counter[] = [0] * 26   # WRONG — Java leak
counter = [0] * 26     # CORRECT
```

---

## CodeSignal Survival Rules

- Solve something correct first, optimize later
- Clarify assumptions before writing any code
- Use a known pattern — do not invent on the spot
- Do not restart a solution midway
- Do not chase clever one-liners under pressure

---

## Progress Tracker

| Day | Topic | Done | Notes |
|---|---|---|---|
| 1 | Dict operations | [ ] | |
| 2 | Iteration patterns | [ ] | |
| 3 | Standard library | [ ] | |
| 4 | HashMap — Two Sum | [ ] | |
| 5 | HashMap — Group Anagrams | [ ] | |
| 6 | Two Pointers — Valid Palindrome | [ ] | |
| 7 | Two Pointers — Container With Most Water | [ ] | |
| 8 | Sliding Window — Longest Substring | [ ] | |
| 9 | Sliding Window — Min Window Substring | [ ] | |
| 10 | BFS — Level Order Traversal | [ ] | |
| 11 | BFS — Number of Islands | [ ] | |
| 12 | Pattern identification drill | [ ] | |
| 13 | Timed mock | [ ] | |
| 14 | Consolidation | [ ] | |
