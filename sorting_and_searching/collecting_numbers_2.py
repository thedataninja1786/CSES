import sys 

data = sys.stdin.read()

def collecting_numbers_with_ops(data):
    ops = []
    data = data.split("\n")
    nums = [int(x) for x in data[1].split()]
    for ls in data[2:]:
        ops.append(list(map(int,ls.split())))
    
    def collecting_numbers(nums):
        nums = [(i,nums[i]) for i in range(len(nums))]
        nums = sorted(nums, key = lambda x:x[1])
        cnt = 1
        for i in range(1,len(nums)):
            if nums[i][0] < nums[i-1][0]:
                cnt += 1

        return cnt

    res = []
    for x,y in ops:
        x -= 1
        y -= 1
        nums[x],nums[y] = nums[y],nums[x]
        res.append(collecting_numbers(nums))
 
    return "\n".join([str(x) for x in res])

print(collecting_numbers_with_ops(data))

    
