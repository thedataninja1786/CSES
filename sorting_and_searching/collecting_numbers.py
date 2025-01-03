import sys 

data = sys.stdin.read()

def collecting_numbers(data):
    data = data.split("\n")[1]
    nums = [int(x) for x in data.split()]

    nums = [(i,nums[i]) for i in range(len(nums))]
    nums = sorted(nums,key = lambda x:x[1])
    
    cnt = 1
    for i in range(1,len(nums)):
        if nums[i-1][0] > nums[i][0]:
            cnt += 1
    
    return cnt 

print(collecting_numbers(data))