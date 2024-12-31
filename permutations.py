n = int(input())

def permutations(n:int)-> str:
    if n == 1:
        return "1"
     
    if n == 2 or n==3:
        return "NO SOLUTION" 
    ls = []
    n += 1
    
    def check(ls):
        for i in range(1,len(ls)):
            if abs(ls[i] - ls[i-1]) == 1:
                return False
        return True

    ls = []
    for i in range(0,n,2):
        if i: ls.append(i)
    for j in range(1,n,2):
        ls.append(j)
    
    
    return " ".join([str(x) for x in ls]) if check(ls) else "NO SOLUTION"

print(permutations(n))