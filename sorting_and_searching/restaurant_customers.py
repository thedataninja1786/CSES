from collections import defaultdict
import sys

data = sys.stdin.read()
data = data.splitlines()

def count_customers(data):
    res = 0
    c = defaultdict(int)
    for l in data[1:]:
        l = list(map(int,l.split()))
        c[l[0]] += 1
        c[l[1]+1] -= 1
    
    cnt = 0 
    for k in sorted(c):
        cnt += c[k]
        res = max(res,cnt)
    
    return res

print(count_customers(data))


