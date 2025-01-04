import sys
from collections import defaultdict

data = sys.stdin.read().split()


def subarray_target_sum_negtaive(data):
    _, t = int(data[0]), int(data[1])
    nums = list(map(int, data[2:]))

    s = 0
    cnt = 0 
    c = defaultdict(int)

    c[0] = 1
    for i in range(len(nums)):
        s += nums[i]

        if s - t in c:
            cnt += c[s - t]

        c[s] += 1


    return cnt

print(subarray_target_sum_negtaive(data))