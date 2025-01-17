import sys

data = sys.stdin.read()
tasks = []

for l in data.splitlines()[1:]:
    l = list(map(int,l.split()))
    tasks.append(l)

tasks = sorted(tasks,key = lambda x:x[0])
time = 0 
res = 0

for t,d in tasks:
    time += t
    res += d - time
    
print(res)



