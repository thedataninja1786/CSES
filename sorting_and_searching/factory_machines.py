import sys
data = sys.stdin.read

data = sys.stdin.read()
data = data.split("\n")
p = int(data[0].split()[-1])

nums = [int(x) for x in data[1].split()]

nums.sort()

"""
10
6 5 1 2 1 5 10 4 6 6
1 1 2 4 5 5 6 6 6 10
"""

l,r = 0,nums[0]*p
while l < r:
    m = (l+r) // 2
    t = 0
    for x in nums:
        t += m // x
        if t >= p: break

    if t >= p:
        r = m
    else:
        l = m + 1

print(l)
