import sys
data = sys.stdin.read()
data= data.split("\n")
nums = [int(x) for x in data[1].split()]

res = 0  
"""
TLE
j = 0
for i in range(1,len(nums)+1):

    while len(set(nums[j:i])) != len(nums[j:i]) and j < i:
        j += 1
    res = max(i - j,res)

print(res)
"""

seen = set()
j = 0 
for i in range(len(nums)):
    while nums[i] in seen:
        seen.remove(nums[j])
        j += 1

    seen.add(nums[i])
    res = max(res, i - j + 1)

print(res)
    