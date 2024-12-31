
# find the max value achievable 
values = [3, 4, 5]
weights = [2, 3, 4]
k = 5
ls = [(v,w) for v,w in zip(values,weights)]
# expected 7

"""
20 12 6
4  3  2

"""
dp = [[0 for _ in range(k+1)] for _ in range(len(weights)+1)]

for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if j < weights[i-1]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i-1][j-weights[i-1]] + values[i-1])

for l in dp:
    print(l)