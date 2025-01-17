from collections import defaultdict
import sys
data = sys.stdin.read()
data = data.split("\n")
T = int(data[0].split()[-1])
nums = [int(x) for x in data[1].split()]
res = []

# x + y + z + k = t
# x + y = t - k - z
"""
correct but TLEs'
def binary_search(nums):
    for i in reversed(range(len(nums))):
        for j in range(i):
            t = T
            t -= nums[i][0]
            t -= nums[j][0]
            l,r = j+1,i-1
            while l < r:
                if nums[l][0] + nums[r][0] == t:
                    lidx = nums[l][1]
                    ridx = nums[r][1]
                    jidx = nums[j][1]
                    iidx = nums[i][1]
                    res.append([lidx,ridx,jidx,iidx])
                    return " ".join([str(x+1) for x in res[0]])
                elif nums[l][0] + nums[r][0] > t:
                    r -= 1
                elif nums[l][0] + nums[r][0] < t:
                    l += 1
    
    return "IMPOSSIBLE"

print(binary_search(nums))
"""
def solution(nums):
    c = defaultdict(list)
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i == j:
                continue
            c[nums[i] + nums[j]].append((i,j))

    
    for k,ls in c.items():
        f = False
        z = T - k
        if z in c and z == k:
            for x,y in c[z]:
                for v in ls:
                    if x not in v and y not in v:
                        f = True
                        break    
        elif z in c:
            x,y = c[z][0]
            for v in ls:
                if x not in v and y not in v:
                    f = True
                    break
        if f: 
            tmp = []
            tmp.append(x)
            tmp.append(y)
            tmp.append(v[0])
            tmp.append(v[1])
            return " ".join([str(x+1) for x in tmp])

    return "IMPOSSIBLE"

print(solution(nums))