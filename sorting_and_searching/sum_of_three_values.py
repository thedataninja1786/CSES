import sys

data = sys.stdin.read()


def three_sum(data):
    data = data.split("\n")
    t = int(data[0].split()[-1])
    nums = [int(x) for x in data[1].split()]

    nums = [(i,nums[i]) for i in range(len(nums))]

    nums = sorted(nums, key = lambda x:x[1])

    i = 0
    res = set()
    T = t
    for k in reversed(range(len(nums))):
        t = T
        t -= nums[k][1]
        
        # now it becomes the two-sum problem -> binary search
        l,r = 0,k-1
        while l < r:
            if nums[l][1] + nums[r][1] == t:
                tmp = [nums[l][0]+1,nums[r][0]+1,nums[k][0]+1]

                res.add(tuple(sorted(tmp)))
                break
            elif nums[l][1] + nums[r][1] < t:
                l += 1
            elif nums[l][1] + nums[r][1] > t:
                r -= 1
                
    if res: 
        res = list(res)[0]
        return " ".join([str(x) for x in res])
    else: return "IMPOSSIBLE"    
        
print(three_sum(data))

