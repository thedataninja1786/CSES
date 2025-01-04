import sys
from bisect import bisect_right

data = sys.stdin.read()

def towers(data):
    data = data.split("\n")
    nums = [int(x) for x in data[1].split()]

    towers = []

    cnt = 0 
    for x in nums:
        idx = bisect_right(towers,x)
        if idx == len(towers):
            towers.append(x)
            cnt += 1
        else:
            towers[idx] = x
        
    return cnt

print(towers(data))