import sys
data = sys.stdin.read()

def max_subarray_sum(data):
    # kadane's algorithm i think??
    nums = []
    data = data.split("\n")[1].split()
    nums = [int(x) for x in data]
    
    res = nums[0]
    s = nums[0] 
    for i in range(1,len(nums)):
        s = max(s+nums[i],nums[i])
        res = max(res,s)
    
    return res

print(max_subarray_sum(data))
