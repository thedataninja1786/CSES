import sys
data = sys.stdin.read()



def subarray_target_sum(data):
    data = data.split("\n")
    t = int(data[0].split()[-1])
    nums = [int(x) for x in data[1].split()]

    j = 0 
    s = 0 
    res= 0
    for i in range(len(nums)):
        if s == t:
            res +=1

        s += nums[i]

        while s > t and j < i:
            s -= nums[j]
            j += 1

    if s == t:
        res += 1    

    return res    

print(subarray_target_sum(data))