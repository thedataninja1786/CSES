s = input()
nums = input()
nums = [int(x) for x in nums.split()]


def divide_apples(nums):
    t = sum(nums) 
    s = {0}
    for v in nums:
        new_sums = set()
        for x in s:
            new_sums.add(x + v)
        s |= new_sums
    return min(abs(t - 2*x) for x in s)

print(divide_apples(nums))