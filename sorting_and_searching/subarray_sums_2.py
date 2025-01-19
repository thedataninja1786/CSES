import sys
from collections import defaultdict,Counter

data = sys.stdin.read().split()
_, t = int(data[0]), int(data[1])
nums = list(map(int, data[2:]))
s = cnt = 0 
c = defaultdict(int)
c[0] = 1
for x in nums:
    s += x

    if s - t in c:
        cnt += c[s-t]

    c[s] += 1

print(cnt)