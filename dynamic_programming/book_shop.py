import sys

data = sys.stdin.read()

def bounded_knapsack(data):
    # 0/1 bounded Knapsack
    lines = data.strip().split('\n')
    # First line has n, budget
    n, budget = map(int, lines[0].split())
    
    # Next n lines each contain price and pages
    prices = []
    pages = []
    for i in range(1, n + 1):
        p, pg = map(int, lines[i].split())
        prices.append(p)
        pages.append(pg)

    dp = [[0 for _ in range(budget+1)] for _ in range(len(pages)+1)]

    for i in range(1,len(dp)):
        # allowed books 
        for j in range(1,len(dp[0])):
            # available $
            if j < prices[i-1]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-prices[i-1]] + pages[i-1])

    return dp[-1][-1]

print(bounded_knapsack(data))