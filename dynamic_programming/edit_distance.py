import sys

data = sys.stdin.read()
# Leventhstein Distance
s1 = data.split("\n")[0]
s2 = data.split("\n")[1]

dp = [[float("inf") for _ in range(len(s1)+1)] for _ in range(len(s2)+1)]

# initialize the empty strings,i.e
# how many moves will it take to make the word from an empty string 
for i in range(len(s1)+1):
    dp[0][i] = i
for i in range(len(s2)+1):
    dp[i][0] = i

for i in range(1,len(dp)):
    for j in range(1,len(dp[0])):
        if s2[i-1] == s1[j-1]:
            dp[i][j] = dp[i-1][j-1]  # no edit if chars match
        else:
            # insert (dp[i][j-1]), delete (dp[i-1][j]), replace (dp[i-1][j-1]) + 1
            dp[i][j] = min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1]) + 1

print(dp[-1][-1])

