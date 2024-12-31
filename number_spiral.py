n = input()
test_cases = input()

coords = []
for t in test_cases.splitlines():
    t = [int(x) for x in t.split()]
    coords.append(t)

def find_num(coords):
    # x = row, y = column
    ls = []
    for x,y in coords:
    
        if x >= y:
            ls.append(str(x*x - y + 1))
        else:
            ls.append(str(y*(y-1) + x))

    return "\n".join(ls)

print(find_num(coords))
