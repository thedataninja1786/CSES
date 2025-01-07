import sys

data = sys.stdin.read()

def combinations2(data):
    MOD = (10**9) + 7
    data = data.split("\n")

    t = int(data[0].split()[-1])
    coins = [int(x) for x in data[1].split()]

    dp = [0 for _ in range(t+1)]
    dp[0] = 1

    for c in coins:
        for i in range(c,t+1):
            dp[i] = (dp[i] + dp[i-c]) % MOD

    return dp[-1]

print(combinations2(data))