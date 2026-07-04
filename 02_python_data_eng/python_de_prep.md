# Data Engineering Python Prep — Log / File Parsing & String Manipulation

The most common DE coding-round topics. Patterns first, then practice problems with
solutions. Everything here is plain Python (no pandas) — that's what these rounds test.

---

## 0. The toolbox (know these cold)

| Tool | Use it for |
|---|---|
| `str` methods | split, strip, join, replace, startswith, find |
| `re` | pattern matching / extraction in logs |
| `collections.Counter` | counting (top-N, frequencies) |
| `collections.defaultdict` | grouping without key checks |
| `csv` | delimited files (handles quoting/edge cases) |
| `json` | JSON / JSONL files |
| `itertools` | grouping, batching, sliding windows |
| generators (`yield`) | streaming large files without loading into memory |
| `datetime` | parsing/handling timestamps |

**Golden rule for DE rounds:** assume the file is too big for memory. **Stream it line by
line** with a generator instead of `f.read()` / `f.readlines()`.

---

## 1. String manipulation — core idioms

```python
s = "  ERROR: disk full on host-12  "

s.strip()                 # 'ERROR: disk full on host-12'  (remove leading/trailing ws)
s.lower() / s.upper()
s.split(":")              # ['  ERROR', ' disk full on host-12  ']
s.split()                 # splits on ANY whitespace, drops empties -> great for log lines
"a,b,,c".split(",")       # ['a', 'b', '', 'c']  (keeps empties — different from .split())
",".join(["a", "b"])      # 'a,b'
s.replace("ERROR", "WARN")
s.startswith("ERROR") / s.endswith("12")
"host-12".find("-")       # 4   (index, or -1 if missing)
"abc"[::-1]               # 'cba'  (reverse)
"key=value".partition("=")# ('key', '=', 'value')  (split on FIRST sep, always 3 parts)
```

### Common string tasks

```python
# Count word frequency
from collections import Counter
words = text.lower().split()
Counter(words).most_common(3)          # [('the', 12), ('a', 9), ('error', 7)]

# Check anagram
sorted("listen") == sorted("silent")

# Reverse words in a sentence
" ".join("the quick fox".split()[::-1])   # 'fox quick the'

# Remove punctuation
import string
clean = text.translate(str.maketrans("", "", string.punctuation))

# Title-case / capitalize
"hello world".title()                  # 'Hello World'

# f-strings & formatting
name, n = "host-1", 42
f"{name}: {n:>5}"                       # 'host-1:    42'  (right-align width 5)
f"{3.14159:.2f}"                        # '3.14'
```

### First non-repeating char (classic)
```python
def first_unique(s):
    counts = Counter(s)
    for ch in s:
        if counts[ch] == 1:
            return ch
    return None
```

---

## 2. File parsing — read efficiently

### Stream a file line by line (the default for DE)
```python
def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        for line in f:               # iterates lazily — one line in memory at a time
            yield line.rstrip("\n")
```

### Delimited / CSV (use the `csv` module — don't hand-split)
`csv` correctly handles quoted fields, embedded commas, and newlines that naive
`line.split(",")` breaks on.
```python
import csv

with open("data.csv", newline="") as f:
    reader = csv.DictReader(f)          # uses header row as keys
    for row in reader:
        print(row["user_id"], row["amount"])

# Writing
with open("out.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["user_id", "total"])
    writer.writeheader()
    writer.writerow({"user_id": "u1", "total": 100})
```

### JSON and JSONL
```python
import json

# Single JSON object/array
with open("config.json") as f:
    data = json.load(f)

# JSONL — one JSON object per line (very common in DE pipelines)
def read_jsonl(path):
    with open(path) as f:
        for line in f:
            if line.strip():
                yield json.loads(line)
```

### Fixed-width fields
```python
line = "u1   100  2026-01-01"
user  = line[0:5].strip()
amt   = int(line[5:10].strip())
date  = line[10:].strip()
```

---

## 3. Log parsing — the #1 DE interview topic

### Pattern A: structured/delimited logs — just split
```
2026-01-15 10:23:01 ERROR host-12 Disk full
```
```python
def parse_line(line):
    parts = line.split(maxsplit=4)     # maxsplit keeps the message intact
    date, time, level, host, msg = parts
    return {"ts": f"{date} {time}", "level": level, "host": host, "msg": msg}
```
> `maxsplit` is the trick: split only the first N fields so the free-text message at the
> end stays whole.

### Pattern B: messy logs — use regex (`re`)
```python
import re

# Apache-style: 127.0.0.1 - - [15/Jan/2026:10:23:01] "GET /api" 200 1043
LOG_RE = re.compile(
    r'(?P<ip>\d+\.\d+\.\d+\.\d+) .* "(?P<method>\w+) (?P<path>\S+)" '
    r'(?P<status>\d+) (?P<size>\d+)'
)

def parse(line):
    m = LOG_RE.search(line)
    if not m:
        return None                    # skip malformed lines, don't crash
    return m.groupdict()               # {'ip':..., 'method':..., 'status':..., ...}
```

**Regex quick reference (memorize these):**

| Pattern | Matches |
|---|---|
| `\d+` | one or more digits |
| `\w+` | word chars (letters/digits/_) |
| `\s+` | whitespace |
| `\S+` | non-whitespace (a "token") |
| `.*` / `.*?` | anything, greedy / non-greedy |
| `[A-Z]+` | one or more uppercase |
| `(?P<name>...)` | named capture group |
| `^` / `$` | start / end of line |
| `\b` | word boundary |

```python
re.search(pat, s)      # first match anywhere (most common)
re.match(pat, s)       # match only at START of string
re.findall(pat, s)     # list of all matches
re.sub(pat, repl, s)   # replace
m.group("name")        # named group  |  m.groupdict() -> all named groups
```

### Pattern C: aggregating logs (the real task)
```python
from collections import Counter, defaultdict

def analyze(path):
    level_counts = Counter()
    errors_by_host = defaultdict(int)
    status_counts = Counter()

    for line in read_lines(path):       # streaming!
        m = LOG_RE.search(line)
        if not m:
            continue
        d = m.groupdict()
        status_counts[d["status"]] += 1
        if d["status"].startswith("5"): # 5xx = server error
            errors_by_host[d["ip"]] += 1

    return {
        "top_status": status_counts.most_common(3),
        "noisiest_hosts": Counter(errors_by_host).most_common(5),
    }
```

---

## 4. Patterns that show up again and again

### Group items by a key (`defaultdict`)
```python
from collections import defaultdict
groups = defaultdict(list)
for row in rows:
    groups[row["category"]].append(row)
```

### Count / top-N (`Counter`)
```python
Counter(items).most_common(5)          # 5 most frequent
```

### Batch a stream into chunks (`itertools`)
```python
from itertools import islice
def batched(iterable, n):
    it = iter(iterable)
    while batch := list(islice(it, n)):
        yield batch

for chunk in batched(read_lines("big.log"), 1000):
    process(chunk)                      # e.g. bulk insert 1000 rows at a time
```

### Sliding window (e.g. detect 3 errors in a row)
```python
from collections import deque
window = deque(maxlen=3)
for line in read_lines(path):
    window.append("ERROR" in line)
    if all(window):
        alert()
```

### Dedupe while preserving order
```python
seen = set()
unique = [x for x in items if not (x in seen or seen.add(x))]
```

---

## 5. Practice problems (with solutions)

### Q1. Count error levels in a log file
> Read a log file, return a count of each log level (INFO/WARN/ERROR).
```python
from collections import Counter

def count_levels(path):
    counts = Counter()
    with open(path) as f:
        for line in f:
            parts = line.split()
            if len(parts) >= 3:
                counts[parts[2]] += 1   # level is 3rd field
    return dict(counts)
```

### Q2. Top N most frequent IPs hitting your server
```python
from collections import Counter

def top_ips(path, n=5):
    ips = Counter()
    with open(path) as f:
        for line in f:
            ip = line.split(maxsplit=1)[0]   # IP is first token
            ips[ip] += 1
    return ips.most_common(n)
```

### Q3. Parse key=value pairs into a dict
> Input: `"user=alice action=login status=ok"`  →  `{'user':'alice', ...}`
```python
def parse_kv(line):
    return dict(pair.split("=", 1) for pair in line.split())
```

### Q4. Extract all error messages between two timestamps
```python
import re
from datetime import datetime

TS = re.compile(r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})")

def errors_between(path, start, end):
    start, end = datetime.fromisoformat(start), datetime.fromisoformat(end)
    for line in read_lines(path):
        m = TS.match(line)
        if not m:
            continue
        ts = datetime.fromisoformat(m.group(1))
        if start <= ts <= end and "ERROR" in line:
            yield line
```

### Q5. Find requests slower than a threshold
> Log ends with response time in ms: `... 200 1043ms`
```python
import re
SLOW = re.compile(r"(\d+)ms\s*$")

def slow_requests(path, threshold_ms=1000):
    for line in read_lines(path):
        m = SLOW.search(line)
        if m and int(m.group(1)) > threshold_ms:
            yield line
```

### Q6. Most common word in a large text file (memory-safe)
```python
from collections import Counter
import re

def top_word(path):
    counts = Counter()
    with open(path) as f:
        for line in f:                  # stream — never load whole file
            counts.update(re.findall(r"[a-z]+", line.lower()))
    return counts.most_common(1)[0]
```

### Q7. Merge two sorted log files by timestamp (classic)
```python
import heapq
def merge_logs(path_a, path_b):
    # heapq.merge lazily merges sorted iterables — O(1) memory
    yield from heapq.merge(read_lines(path_a), read_lines(path_b))
```

### Q8. Count unique visitors per day
```python
from collections import defaultdict

def unique_visitors(path):
    visitors = defaultdict(set)
    for line in read_lines(path):
        date, ip = line.split()[0], line.split()[3]
        visitors[date].add(ip)
    return {day: len(ips) for day, ips in visitors.items()}
```

---

## 6. Scale / performance talking points (DE differentiator)

Mention these even in a small problem — it signals DE maturity:

- **Stream, don't load.** `for line in f` over `f.readlines()` — O(1) memory vs O(file).
- **Generators (`yield`)** keep pipelines lazy and chainable: `parse(filter(read(path)))`.
- **`Counter` / `defaultdict`** are O(1) per update — avoid re-scanning lists.
- **Batch writes** (e.g. bulk insert 1000 rows) instead of row-by-row I/O.
- **Compile regex once** (`re.compile` at module level), not inside the loop.
- **Skip malformed lines gracefully** (`if not m: continue`) — real log files are dirty.
- **For truly huge / parallel:** this is where you'd reach for **Spark/PySpark** — same
  logic, distributed. (Good place to bridge to your Spark experience.)

---

## 7. Common gotchas

- `.split()` (no arg) splits on any whitespace and **drops empty strings**;
  `.split(",")` keeps empties. Know the difference.
- `re.match` anchors at the **start**; use `re.search` to match anywhere.
- Default `open()` uses the OS encoding — pass `encoding="utf-8"` to be safe.
- Greedy `.*` over-matches; use non-greedy `.*?` when you want the shortest match.
- `int("100ms")` throws — extract digits first (`re` or slicing).
- Mutating a list while iterating it → bugs. Build a new list / filter instead.
- `dict` preserves insertion order (Python 3.7+) — relevant for "preserve order" asks.

---

## 8. 60-second interview checklist

1. **Clarify:** file size? format consistent? malformed lines? expected output?
2. **Default to streaming** (`for line in f`) unless told it fits in memory.
3. **Pick the tool:** split for clean delimited, `re` for messy, `csv`/`json` for those formats.
4. **Aggregate with** `Counter` / `defaultdict`.
5. **Handle bad lines** (skip, don't crash).
6. **State the scale story** (streaming, batching, "Spark if it's TB-scale").
7. **Test on 2–3 lines** including an edge case (empty line, malformed).
