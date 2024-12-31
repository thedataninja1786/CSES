import sys
sys.setrecursionlimit(10000)

n = 26560

def two_sets(n:int) -> str:
    global res
    nums = [i+1 for i in range(n)]
    res = []

    def dfs(i,ls,ds):
        global res
        if i == len(nums) and sum(ls) == sum(ds):
            res = [ds,ls]
            return
        if i >= len(nums):
            return 
        
        dfs(i+1,ls + [nums[i]],ds)
        dfs(i+1,ls, ds + [nums[i]])
        

    dfs(0,[],[])
    
    res = sorted(res, key =lambda x:len(x),reverse=True)
    
    if not res:
        return "NO"
    else:
        s = "YES"
        for ls in res:
            s += "\n" + str(len(ls)) + "\n" + " ".join([str(x) for x in ls])
        return s
    
print(two_sets(n))