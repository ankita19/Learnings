'''
Day 1 — Dictionary operations
  Drill : write these 10 times each from scratch
    d = {}
    d[key] = value
    key in d
    d.get(key, default)
    for k, v in d.items()
    from collections import defaultdict, Counter

Day 2 — Iteration patterns
  Drill : write these until automatic
    for i, val in enumerate(arr)
    sorted(arr, key=lambda x: x[1])
    [x for x in arr if x > 0]
    arr[::-1]  ,  arr[i:j]

Day 3 — Standard library you'll actually use
  Drill :
    from collections import deque
    q = deque(); q.append(x); q.popleft()
    import heapq
    heapq.heappush(h, val); heapq.heappop(h)
    from collections import Counter
    Counter("aabbc")  →  understand what it returns



#define dictionary
d = {}
#assign value to dictionary
d['key'] = 'value'

#contains
key in d

#get
d.get(key , default)

for k, v in d.items():

from collections import defaultdict, Counter

Iteration patterns
for i , val in enumerate(arr)
sorted(arr,key=lambda x:x[1])
[x for x in arr if x> 0] shows how to use list comprehension to filter out values greater than 0 from arr
arr[::-1] reverse list
arr[i:j] slicing list from index i to j

from collections import deque
q = deque(); q.app
'''

