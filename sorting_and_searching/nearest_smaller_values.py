import sys 

data = sys.stdin.read()

data = data.split("\n")
nums = [int(x) for x in data[1].split()]

s = []
res = []

for i in range(len(nums)):
    
    while s and nums[s[-1]] >= nums[i]:
        s.pop()
    
    if not s:
        res.append(0)    
    else:
        res.append(s[-1]+1)
    s.append(i)

print(" ".join([str(x) for x in res]))