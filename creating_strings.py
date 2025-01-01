s = input()

def create_strings(s:str):
    global res
    res = set()
    ls = list(s)
    
    def dfs(ls,s):
        global res
        if not ls:
            res.add(s)
            return 
    
        for _ in range(len(ls)):
            x = ls.pop(0)
            dfs(ls, s + x)
            ls.append(x)
        
    dfs(ls,"")
    return res

ls = sorted(create_strings(s))
print(len(ls))
for x in ls:
    print(x)
            