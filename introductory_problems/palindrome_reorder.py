from collections import Counter 

s = input()

def is_pali(s:str) -> str:
    c = Counter(s)

    # if there are more than two elements with odd count => No Solution
    odd_cnt = 0 
    for k,v in c.items():
        if v % 2 != 0:
            odd_cnt += 1

    if odd_cnt > 1:
        return "NO SOLUTION"

    s1,s2 = "",""

    # reverse s2 in the end 
    for k,v in c.items():
        if v % 2 != 0:
            continue
        s1 += k * (v//2)
        s2 += k * (v//2)
        
    for k,v in c.items():
        if v % 2 != 0:
            s1 += k*v

    res = s1 + s2[::-1]
    return res if res == res[::-1] else "NO SOLUTION"

print(is_pali(s))