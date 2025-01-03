
n = input()
s = input()

def increase(s:str) -> str:
    nums = [int(x) for x in s.split()]
    cnt = 0 
    for i in range(1,len(nums)):
        if nums[i] < nums[i-1]:
            cnt += nums[i-1] - nums[i]
            nums[i] = nums[i-1]
    return str(cnt) 

print(increase(s))