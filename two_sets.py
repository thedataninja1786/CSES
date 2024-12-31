n = int(input())

def two_sets(n):
    nums = [i+1 for i in range(n)]
    s = sum(nums)//2
    if s != sum(nums)/2:
        return "NO"
    ls,ds = [],[]
    
    for i in reversed(range(len(nums))):
        if s - nums[i] >= 0:
            ds.append(nums[i])
            s -= nums[i]
        else:
            ls.append(nums[i])
    
    if s:
        return "NO"
    else:
        res = [ls,ds]
        res = sorted(res,key=lambda x:len(x),reverse=True)
        out = "YES"
        for ls in res:
            out += "\n" + str(len(ls)) + "\n" + " ".join([str(x) for x in ls])
        return out

print(two_sets(n))