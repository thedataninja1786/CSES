n = int(input())

def remove_digits(n):
    dp = [float("inf") for _ in range(n+1)]
    dp[0] = 0 

    for i in range(1,n+1):
        x = i
        digits = []
        while x != 0:
            digits.append(x % 10)
            x //= 10
        
        for d in digits:
            dp[i] = min(dp[i],dp[i-d]+1) # +1 accounts for the one subtraction operation


    return dp[-1]

print(remove_digits(n))