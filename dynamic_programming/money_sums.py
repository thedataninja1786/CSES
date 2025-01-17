import sys

data = sys.stdin.read()

data = data.split("\n")
coins = sorted([int(x) for x in data[1].split()])

t = sum(coins)
dp = [False for _ in range(t+1)]
dp[0] = True

for c in coins:
    for i in reversed(range(c,t+1)):
        if dp[i-c]:
            dp[i] = True
    
print(len([str(i) for i in range(1,len(dp)) if dp[i]]))
print(" ".join([str(i) for i in range(1,len(dp)) if dp[i]]))