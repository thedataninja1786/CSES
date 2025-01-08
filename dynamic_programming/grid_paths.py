import sys

data = sys.stdin.read()

def find_paths(data):
    grid = []
    for line in data.splitlines():
        if line:
            grid.append(list(line)) 

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == ".":
                grid[i][j] = 0
            if grid[i][j] == "*":
                grid[i][j] = -1

    for i in range(len(grid)):
        if grid[i][0] == -1:
            break
        grid[i][0] = 1

    for j in range(len(grid[0])):
        if grid[0][j] == -1:
            break 
        grid[0][j] = 1


    for i in range(1,len(grid)):
        for j in range(1,len(grid[0])):
            if grid[i][j] == -1: continue

            if grid[i-1][j] != -1:
                grid[i][j] += grid[i-1][j]
            if grid[i][j-1] != -1:
                grid[i][j] += grid[i][j-1]

    res = grid[-1][-1]
    return str(res) if res != -1 else str(0)


print(find_paths(data))

