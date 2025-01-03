from typing import List

n = int(input())
nums = input()
nums = [int(x) for x in nums.split()]

def missing_number(nums:List[int],n:int) -> str:
    nums = set(nums)
    for i in range(2,n+1):
        if i not in nums:
            return str(i)
    return str(1)

print(missing_number(nums,n))