import sys

data = sys.stdin.read()

def sparse_table_for_min_range_queries(data):
    # static range minimum queries (RMQ)
    data = data.split("\n")
    nums = [int(x) for x in data[1].split()]
    queries = []
    for l in data[2:]:
        if l: queries.append(list(map(int,l.split())))

    # precompute logs
    # for n = 8 we utilize the property:
    # 8 -> 4 -> 2 -> 1
    logs = [0] * (len(nums)+1)
    for i in range(2,len(nums)+1):
        logs[i] = logs[i//2] + 1

    # build the sparse tasble
    N = len(nums)
    k = logs[N] + 1 # max power of 2 needed
    st = [[0]*k for _ in range(len(nums))]
    for i in range(len(nums)):
        st[i][0] = nums[i] # base case: range of size 1

    # filling the table
    j = 1
    while (1 << j) <= N: # 2^j musto not exceed n 
        for i in range(N - (1 << j) + 1): # include valid stating points only
            st[i][j] = min(st[i][j-1], st[i + (1 << (j-1))][j-1])
        j += 1

    res = []
    for l,r in queries:
        l -= 1
        r -= 1
        j = logs[r-l+1]
        res.append(min(st[l][j], st[r-(1<<j)+1][j]))

    return "\n".join([str(x) for x in res])

print(sparse_table_for_min_range_queries(data))