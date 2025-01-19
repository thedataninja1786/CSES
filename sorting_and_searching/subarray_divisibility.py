import sys
from collections import defaultdict
data = sys.stdin.read()

data = data.split("\n")
t = int(data[0].split()[-1])
nums = [int(x) for x in data[1].split()]

"""
For each prefix sum, calculate its modulo 𝑛
n. If two prefix sums have the same remainder when divided by 𝑛
n, the subarray between those two indices is divisible by 𝑛.
"""

s = cnt = 0 
c= defaultdict(int)
c[0] = 1
for x in nums:
    s += x

    # This guarantees that the remainder will be in the expected 
    # range of [0, t-1], avoiding issues with negative values.
    r = (s % t + t) % t

    if r in c:
        cnt += c[r]
    
    c[r] += 1

print(cnt)