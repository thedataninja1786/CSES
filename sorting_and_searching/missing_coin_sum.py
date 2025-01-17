import sys

data = sys.stdin.read()
data = data.split("\n")
nums = [int(x) for x in data[1].split()]
nums.sort()

def solve(nums):
    if 1 not in nums:
        return 1
    s = 1
    for i in range(len(nums)-1):
        s += nums[i]
        if s < nums[i+1]:
            return s

    return sum(nums)+1

print(solve(nums))

