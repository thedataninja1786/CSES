import sys 
data = sys.stdin.read()

def distinct_numbers(data):
    data = data.split("\n")[1].split()
    nums = set(data)
    return len(nums)

print(distinct_numbers(data)) 