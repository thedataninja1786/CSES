from collections import defaultdict

import sys

data = sys.stdin.read()

def distinct_subarrays(data):
    data = data.split("\n")
    k = int(data[0].split()[-1])
    nums = [int(x) for x in data[1].split()]

    j = 0 
    c = defaultdict(int)
    cnt = 0
    for i in range(len(nums)):
        c[nums[i]] += 1

        while len(c.keys()) > k:
            c[nums[j]] -= 1
            if c[nums[j]] == 0:
                del c[nums[j]]
            j += 1
        
        if len(c.keys()) <= k:
            cnt += i - j + 1

    return cnt 

print(distinct_subarrays(data))