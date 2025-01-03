from collections import defaultdict
import sys 

data = sys.stdin.read()

def sum_two_vals(data):
    data =data.split("\n")
    nums = [int(x) for x in data[1].split(" ")]
    t = int(data[0].split()[-1])

    c = defaultdict(int)
    res = []
    for i,x in enumerate(nums):
        if x in c:
            j,v = c[x]
            res.append([j+1,i+1])

        c[t-x] = (i,x)

    return "IMPOSSIBLE" if not res else  str(res[0][0]) + " " + str(res[0][1])      

print(sum_two_vals(data))