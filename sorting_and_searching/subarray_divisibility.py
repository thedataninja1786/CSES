import sys 
from collections import defaultdict 

data = sys.stdin.read() 

def subarray_divisibility(data):
    # idea:
    # 1. convert to base t x % t 
    # 2. prefix sum and convert to base t again
    # 3. if the number appears again, 
    #    means divisible by t since x2 - x1 == 0
    
    
    data = data.split("\n")
    t = int(data[0])
    nums = [int(x) for x in data[1].split()]
    cnt = 0 
    c = defaultdict(int)
    
    c[0] = 1
    s = 0
    nums = [x%t for x in nums]
    dp = []

    for x in nums:
        s += x
        dp.append(s)
    
    nums = [x%t for x in dp]
    for i in range(len(nums)):

        if nums[i] in c: 
            cnt += c[nums[i]]

        c[nums[i]] += 1

    return cnt 
    
print(subarray_divisibility(data))
