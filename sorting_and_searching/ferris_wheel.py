import sys

data = sys.stdin.read()

def ferris_wheel(data):
    res = 0
    data = data.split("\n")
    _,limit = data[0].split()
    limit = int(limit)    
    nums = [int(x) for x in data[1].split()]
    nums.sort()

    l,r = 0,len(nums)-1
    while l <= r:
        if nums[r] > limit:
            r -= 1
            continue
        elif nums[r] <= limit and nums[l] + nums[r] > limit:
            res += 1
            r -= 1
        elif nums[r] + nums[l] <= limit:
            res += 1
            l += 1 
            r -= 1
        
    return res

print(ferris_wheel(data))

    
