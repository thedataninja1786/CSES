from statistics import median
import sys

data = sys.stdin.read()

def minimize_cost(data):
    data = data.split("\n")[1].split()
    nums = list(map(int,data))
    m = median(nums)
    res = 0 
    for x in nums:
        res += abs(x-m)

    return int(res)


print(minimize_cost(data))