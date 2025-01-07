import sys

data = sys.stdin.read()

def min_coin_sum(data):
    data = data.split("\n")
    t = int(data[0].split()[-1])
    coins = [int(x) for x in data[1].split()]

    dp = [float("inf") for _ in range(t+1)]
    dp[0] = 0

    for c in coins:
        for i in range(c,len(dp)):
            if i - c >= 0:
                dp[i] = min(dp[i],dp[i-c] + 1)

    return dp[-1] if dp[-1] != float("inf") else -1

print(min_coin_sum(data))

