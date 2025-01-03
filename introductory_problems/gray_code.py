from functools import lru_cache

n = 8
res = set()

def check(ls):
    ls = list(map(int,ls))
    for i in range(1,len(ls)):
        if not (0 <= abs(ls[i] - ls[i-1]) <= 1):
            return False
    return True

@lru_cache
def dfs(ls):
    global res
    
    if len(ls) == n and check(ls):
        res.add(ls)
        return 

    for _ in range(n):
        dfs(ls + "1")
        dfs(ls + "0")

dfs("")
print(res)