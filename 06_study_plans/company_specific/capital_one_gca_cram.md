# Capital One CodeSignal GCA — One Day Cram Sheet
> Test tomorrow. Use this doc only. No new problems.

---

## Test Format
- **4 questions, 70 minutes** — all 4 visible simultaneously, switch freely
- Auto-scored on hidden test cases (partial credit per test case passed)
- Scoring scale: **200–600**. Capital One cutoff is reportedly **570+**
- Sometimes manually reviewed for later rounds — use clear variable names
- **Proctoring is required:** webcam + mic + screen share. Setup takes 5-10 min.
  - Close all other apps before you start
  - Do not look away from screen — eye movement flags you
  - Have your ID ready for identity verification

## Time Strategy: "1-2-4-3"
| Order | Q | Target time | Why |
|---|---|---|---|
| 1st | Q1 | ≤ 8 min | Pure warmup — never spend more |
| 2nd | Q2 | ≤ 15 min | HashMap — your strongest pattern |
| 3rd | Q4 | ≤ 25 min | Algorithmic — tackle while mentally fresh |
| 4th | Q3 | Remaining | Implementation-heavy — grind through last |

> **Rule:** Read Q3 and Q4 before starting Q3. If Q4 looks cleaner (it usually does), do Q4 first.
> **Caveat:** If Q4 completely stumps you after 10 minutes, switch to Q3 and come back. Don't burn 25 min on a blank page.
>
> Q3 is the #1 time killer — candidates report spending 35+ min on it and having nothing left for Q4. Avoid this.

---

## Pattern 1 — Array Transformation (Q1)

**What it looks like:** Given array `a`, return `b` where `b[i] = a[i-1] + a[i] + a[i+1]`, treating out-of-bounds as 0.

**Template:**
```python
def array_transform(a):
    n = len(a)
    b = [0] * n
    for i in range(n):
        left  = a[i-1] if i > 0 else 0
        right = a[i+1] if i < n-1 else 0
        b[i] = left + a[i] + right
    return b
```

**What trips people:** forgetting the bounds check. Always: `if i > 0` and `if i < n - 1`.

---

## Pattern 2 — HashMap / Frequency Count (Q2)

**What it looks like:** Group transactions by user, find top-K most frequent, count occurrences.

**Core template — memorize this:**
```python
count = {}
for item in items:
    count[item] = count.get(item, 0) + 1
```

**Top-K variant (with heap):**
```python
import heapq

count = {}
for item in items:
    count[item] = count.get(item, 0) + 1

# k largest
heap = []
for key, freq in count.items():
    heapq.heappush(heap, (freq, key))
    if len(heap) > k:
        heapq.heappop(heap)

return [item for freq, item in heap]
```

**Grouping variant (like Group Anagrams):**
```python
from collections import defaultdict

groups = defaultdict(list)
for item in items:
    key = get_group_key(item)   # e.g., sorted(item), item['user'], etc.
    groups[key].append(item)

return list(groups.values())
```

**Watch out:** amounts may come as strings → convert with `int(amount)` before summing.

---

## Pattern 3 — Sliding Window (Q4)

**What it looks like:** Longest subarray/substring meeting a condition. "No more than K distinct", "sum ≤ K", "no repeats".

**The skeleton — this is what you burn in:**
```python
left = 0                     # ← always starts at 0. always.
window = {}                  # track what's inside the window
result = 0

for right in range(len(s)):
    # Step 1: expand — add s[right] into window
    window[s[right]] = window.get(s[right], 0) + 1

    # Step 2: shrink — while window is INVALID, move left
    while len(window) > k:                   # condition changes per problem
        window[s[left]] -= 1
        if window[s[left]] == 0:
            del window[s[left]]
        left += 1

    # Step 3: update result
    result = max(result, right - left + 1)   # window size = right - left + 1

return result
```

**The 3 moves never change:** expand → shrink while invalid → update result.

**Common variants:**
| Problem type | Window validity condition | What to track |
|---|---|---|
| No repeats | `window[char] > 1` | char → count dict |
| At most K distinct | `len(window) > k` | char → count dict |
| Sum ≤ K | `window_sum > k` | running integer sum |
| Min window containing target | `missing > 0` | two count dicts |

**Kadane's Algorithm (max subarray sum — may appear):**
```python
def max_subarray(nums):
    max_sum = nums[0]
    curr = nums[0]
    for num in nums[1:]:
        curr = max(num, curr + num)   # restart or extend
        max_sum = max(max_sum, curr)
    return max_sum
```

---

## Pattern 3b — Monotonic Stack (Q4 variant)

**What it looks like:** Largest rectangle in histogram, next greater element, trapping rain water.

```python
def largest_rectangle(heights):
    stack = []   # stores indices
    max_area = 0

    for i, h in enumerate(heights):
        start = i
        while stack and stack[-1][1] > h:
            idx, height = stack.pop()
            max_area = max(max_area, height * (i - idx))
            start = idx
        stack.append((start, h))

    for idx, height in stack:
        max_area = max(max_area, height * (len(heights) - idx))

    return max_area
```

**The pattern:** use a stack to track elements waiting to be resolved. Pop when current element is smaller/larger than top.

---

## Pattern 4 — Matrix Manipulation (Q3)

**What it looks like:** Rotate 90°, apply "gravity", shift rows/columns.

**Rotate 90° clockwise — the one to know:**
```python
def rotate(matrix):
    n = len(matrix)
    # Step 1: transpose (flip along diagonal)
    for i in range(n):
        for j in range(i+1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: reverse each row
    for row in matrix:
        row.reverse()
```

**"Gravity" / drop elements (Candy Crush style):**
```python
# Compress non-zero elements to bottom of each column
for col in range(cols):
    bottom = rows - 1
    for row in range(rows - 1, -1, -1):
        if grid[row][col] != 0:
            grid[bottom][col] = grid[row][col]
            if bottom != row:
                grid[row][col] = 0
            bottom -= 1
```

**Spiral Matrix traversal (Q3 common pattern):**
```python
def spiral_order(matrix):
    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:
        # → go right across top row
        for c in range(left, right + 1):
            result.append(matrix[top][c])
        top += 1

        # ↓ go down right column
        for r in range(top, bottom + 1):
            result.append(matrix[r][right])
        right -= 1

        # ← go left across bottom row (if still valid)
        if top <= bottom:
            for c in range(right, left - 1, -1):
                result.append(matrix[bottom][c])
            bottom -= 1

        # ↑ go up left column (if still valid)
        if left <= right:
            for r in range(bottom, top - 1, -1):
                result.append(matrix[r][left])
            left += 1

    return result
```

**The 4 moves:** right → down → left → up. After each move, shrink the boundary. Check `top <= bottom` and `left <= right` before the 3rd and 4th moves to avoid duplicating rows/cols in non-square matrices.

---

**2D Prefix Sum (Q3 common pattern — region sum queries):**
```python
# Build prefix sum matrix
def build_prefix(grid):
    rows, cols = len(grid), len(grid[0])
    prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
    for r in range(rows):
        for c in range(cols):
            prefix[r+1][c+1] = (grid[r][c]
                                + prefix[r][c+1]
                                + prefix[r+1][c]
                                - prefix[r][c])
    return prefix

# Query: sum of rectangle (r1,c1) to (r2,c2) inclusive, 0-indexed
def query(prefix, r1, c1, r2, c2):
    return (prefix[r2+1][c2+1]
            - prefix[r1][c2+1]
            - prefix[r2+1][c1]
            + prefix[r1][c1])
```

**BFS on grid (Number of Islands):**
```python
from collections import deque

def num_islands(grid):
    rows, cols = len(grid), len(grid[0])
    visited = set()
    count = 0

    def bfs(r, c):
        q = deque([(r, c)])
        visited.add((r, c))
        while q:
            row, col = q.popleft()
            for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                nr, nc = row+dr, col+dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == "1":
                    visited.add((nr, nc))
                    q.append((nr, nc))

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1" and (r,c) not in visited:
                bfs(r, c)
                count += 1
    return count
```

---

## String Simulation (Q2 or Q3 variant)

**What it looks like:** "Remove last char and prepend to front until condition met." Follow the rules exactly — no shortcuts.

```python
# Generic simulation skeleton
s = list(input_string)
while not condition_met(s):
    # apply transformation step
    char = s.pop()        # remove from end
    s.insert(0, char)     # add to front
```

> `insert(0, x)` is O(n). If performance matters, use `deque` with `appendleft`.

```python
from collections import deque
d = deque(input_string)
while not condition_met(d):
    d.appendleft(d.pop())
```

---

## Python Syntax You Cannot Afford to Blank On

```python
# Dict
count = {}
count[k] = count.get(k, 0) + 1
k in count
for k, v in count.items():

# defaultdict
from collections import defaultdict
d = defaultdict(list)
d[key].append(val)

# deque
from collections import deque
q = deque()
q.append(x)       # right
q.appendleft(x)   # left
q.popleft()       # left
q.pop()           # right

# heap (always min-heap)
import heapq
heap = []
heapq.heappush(heap, val)
heapq.heappop(heap)
heap[0]           # peek

# max-heap: negate
heapq.heappush(heap, -val)
-heapq.heappop(heap)

# enumerate
for i, val in enumerate(arr):

# 2D grid init
grid = [[0] * cols for _ in range(rows)]

# swap
a, b = b, a
```

---

## Your Weak Area Reminders

- `left = 0` — always first line of sliding window. Non-negotiable.
- `[]` never on LEFT of assignment: `counter = [0] * 26` not `counter[] = ...`
- `count.get(k, 0) + 1` — read left to right: "get current, add 1"
- Heap in Python is a **plain list**, not an object. `heapq` is the module.
- When popping a tuple: `heapq.heappop(heap)[1]` to get second element.

---

## During the Test

1. **Read all 4 problems in the first 5 minutes** before writing any code.
2. **Decide Q3 vs Q4 order** using the 1-2-4-3 method above.
3. **State your pattern** (even just in a comment) before coding.
4. **Get something passing first** — partial credit from test cases > elegant incomplete code. A brute force earns 40-60% of points.
5. **Never restart midway.** Patch and move forward.
6. **Clear variable names** — reviewers may read the code for later rounds.
7. **Test your own edge cases before submitting** — the auto-grader does NOT tell you which cases failed. Always test: empty input, single element, all same values, negatives.

---

## Today's Practice (do these in order, timed)

| # | Problem | Pattern | Target time |
|---|---|---|---|
| 1 | [Two Sum](https://leetcode.com/problems/two-sum/) | HashMap | 8 min |
| 2 | [Top K Frequent Elements](https://leetcode.com/problems/top-k-frequent-elements/) | HashMap + Heap | 15 min |
| 3 | [Longest Substring Without Repeating Chars](https://leetcode.com/problems/longest-substring-without-repeating-characters/) | Sliding Window | 15 min |
| 4 | [Rotate Matrix](https://leetcode.com/problems/rotate-image/) | Matrix | 20 min |
| 5 | [Max Subarray (Kadane's)](https://leetcode.com/problems/maximum-subarray/) | Kadane | 10 min |

> After each: close the solution and **retype from scratch**. This is not optional.

---

## Tonight (30 min before sleep)

1. Write all 4 templates from memory — no peeking.
2. Read the "Weak Area Reminders" section once.
3. Stop. Sleep. Cramming after this makes it worse.
