import sys

data = sys.stdin.read()

def array_division(data):
    # feasibility search
    data = data.split("\n")
    k = int(data[0].split()[-1])
    nums = [int(x) for x in data[1].split()]

    l,r = max(nums),sum(nums)
    while l < r:
        subarrays = []
        m = (l+r)//2

        s = 0 
        for i in range(len(nums)):
            if s + nums[i] > m:
                subarrays.append(s)
                s = nums[i]
                
            else: s += nums[i]
        
        if subarrays[-1] != s: subarrays.append(s)
        
        if len(subarrays) > k:
            # If more subarrays are formed than allowed increase l
            l = m + 1
        else:
            r = m
     
    return l

print(array_division(data))

