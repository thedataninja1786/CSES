from bisect import bisect_right
import heapq
import sys

data = sys.stdin.read()

nums = []
for l in data.splitlines()[1:]:
    nums.append(list(map(int,l.split())))
nums = [(nums[i][0],nums[i][1],i) for i in range(len(nums))]
res = [0] * len(nums)

nums.sort(key = lambda x:x[0])
rooms = []
available = []
heapq.heapify(rooms)


mx = 0

for a,d,idx in nums:
    if rooms and rooms[0][0] < a:
        _,rm = heapq.heappop(rooms)
        heapq.heappush(rooms,(d,rm))
        res[idx] = rm
    else:
        mx += 1
        res[idx] = mx
        heapq.heappush(rooms,(d,mx))

print(mx)
print(" ".join([str(x) for x in res]))


