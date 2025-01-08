import sys 
import bisect

data = sys.stdin.read()

data = data.split("\n")
nums = [int(x) for x in data[1].split()]

"""
O(n^2) TLEs'
dp = [1 for _ in range(len(nums))]

for i in range(1,len(nums)):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j] + 1)

print(max(dp))
"""

tmp = []
for x in nums:
    idx = bisect.bisect_left(tmp,x)
    if idx == len(tmp):
        tmp.append(x)
    else:
        tmp[idx] = x 
    
print(len(tmp))