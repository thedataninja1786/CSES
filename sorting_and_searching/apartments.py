import heapq
import sys
data = sys.stdin.read()
data = data.split("\n")
k = int(data[0].split()[-1])
clients = [int(x) for x in data[1].split()]
apartments = [int(x) for x in data[2].split()]
clients.sort(reverse=True)
apartments.sort(reverse=True)

cnt = 0 

i = j = 0
while i < len(clients) and j < len(apartments):
    if abs(clients[i]-apartments[j]) <= k:
        cnt +=1 
        j += 1
        i += 1
    elif clients[i] - apartments[j] > k:
        i += 1
    else:
        j += 1

print(cnt)