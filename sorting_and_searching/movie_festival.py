from collections import defaultdict
import sys 

data = sys.stdin.read()


def movie_festival(data):
    ls = []
    for l in data.splitlines()[1:]:
        ls.append(list(map(int,l.split())))
    
    ls.sort(key = lambda x:x[1])
    x = float("-inf")
    res = len(ls)
    for i in range(len(ls)):
        if ls[i][0] < x:
            res -= 1
        else:
            x = ls[i][-1]
    
    return res

print(movie_festival(data))