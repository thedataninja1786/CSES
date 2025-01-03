dirs = {(1, 0): "D", (-1, 0): "U", (0, 1): "R", (0, -1): "L"}
coords = [(1, 0), (-1, 0), (0, 1), (0, -1)]
R, C = 7,7  
target = (6, 0)  

def is_dead_end(i, j, visited):
    """
    Checks if moving into a cell creates an isolated section of the grid.
    """
    unvisited_neighbors = 0
    for dx, dy in coords:
        x, y = i + dx, j + dy
        if 0 <= x < R and 0 <= y < C and (x, y) not in visited:
            unvisited_neighbors += 1
    # Dead-end: A cell with only one valid unvisited neighbor
    return unvisited_neighbors <= 1

res = []
def dfs(i, j,p,visited):
    global res
    if len(p) > 5 and p[5] != "R":
        return 

    if (i, j) == target:
        if len(visited) == R * C:
            res.append(p)
        return

    # Explore all directions
    for dx, dy in coords:
        x, y = i + dx, j + dy
        if 0 <= x < R and 0 <= y < C and (x, y) not in visited:
            # Add the cell to the visited set
            visited.add((x, y))

            # Prune dead-end paths
            #if not is_dead_end(x, y, visited):
            dfs(x, y, p + dirs[(dx,dy)],visited)

            # Backtrack
            visited.remove((x, y))



dfs(0, 0,"",set([(0, 0)]))
print(len(res))
