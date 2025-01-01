import sys

def coin_piles(data:str) -> str:
    ls = []
    for line in data.splitlines()[1:]:
        ls.append(list(map(int,line.split())))

    res = []
    for p1,p2 in ls:
        if (p1+p2) % 3 == 0 and (p1 <= 2*p2 and p2 <= 2*p1):
            res.append("YES")
        else:
            res.append("NO")
    
    return "\n".join(res)

data = sys.stdin.read()

print(coin_piles(data))
        
        
