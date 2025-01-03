from bisect import bisect_right
from collections import Counter, defaultdict
import sys
 
data = sys.stdin.read()
 
def concert_tickets(data):
    data = data.split("\n")
    
    tickets = [int(x) for x in data[1].split()]
    customers = [int(x) for x in data[2].split()]
 
    tickets.sort(reverse=False)
    c = defaultdict(int)
    for t in tickets:
        c[t] += 1
    
    res = []
    for x in customers:
        idx = bisect_right(list(c.values()),x)-1
        if idx >= 0 and c[tickets[idx]] > 0:
            res.append(tickets[idx])
            c[tickets[idx]] -= 1
            if c[tickets[idx]] == 0:
                del c[tickets[idx]]
            
        else:
            res.append(-1)
 
    return "\n".join([str(x) for x in res])
 
print(concert_tickets(data))