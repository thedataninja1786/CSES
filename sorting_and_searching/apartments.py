import sys
#data = sys.stdin.read()

data = """10 10 0
37 62 56 69 34 46 10 86 16 49
50 95 47 43 9 62 83 71 71 7"""

def optimize_max(data):
    data = data.split("\n")
    n, m, d = map(int, data[0].split())
    desired_size = [int(x) for x in data[1].split()]
    available = [int(x) for x in data[2].split()]

    desired_size.sort(reverse=False)
    available.sort(reverse=False)

    res = 0
    while available and desired_size:
        a = available.pop(0)
        print(a,desired_size)
        if abs(a-desired_size[0]) <= d:
            res += 1
        elif a - d < desired_size[0]:
            available.insert(0,a)
        
        desired_size.pop(0)
        

    return res

print(optimize_max(data))