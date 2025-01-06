import sys 

data = sys.stdin.read()


def estimate(data):
    data = data.split("\n")
    nums = [int(x) for x in data[1].split()]
    queries = []
    for l in data[2:]:
        if l: queries.append(list(map(int,l.split())))
    s = 0 

    dp = []
    for i in range(len(nums)):
        s += nums[i]
        dp.append(s)

    res = []
    for x,y in queries:
        x-=1;y-=1
        if x - 1 >= 0:
            res.append(dp[y] - dp[x-1])
        else: res.append(dp[y])

    return "\n".join([str(x) for x in res])

print(estimate(data))