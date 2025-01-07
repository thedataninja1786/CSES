from functools import lru_cache

t = int(input())

def dice_combinations(t):
    MOD = (10**9)+7

    dp = [0 for _ in range(t+1)]
    dp[0] = 1

    for i in range(1,t+1):
        for j in range(1,7):
            if i-j >= 0:
                dp[i] = (dp[i] + dp[i-j]) % MOD
    
    return dp[-1]


print(dice_combinations(t))

