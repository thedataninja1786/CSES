import sys
data = sys.stdin.read()
grid = [list(x) for x in data.splitlines()]

def n_queens(grid):
    global res
    n = len(grid)
    coords = []
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == "*":
                coords.append((i,j))

    cols = [False for _ in range(n)]
    diag1 = [False] * (2 * n - 1) # row - col diagonals
    diag2 = [False] * (2 * n - 1) # row + col diagonals 

    board = [-1] * n # stores queens positions (column indices)
    res = 0 

    def backtrack(r):
        global res
        if r == n:
            res += 1 
            return 
        
        for c in range(n):
            # check if placing the queen at (r,c) is valid
            if (r,c) not in coords and not cols[c] and not diag1[r - c + (n-1)] and not diag2[r + c]:
                board[r] = c
                cols[c] = diag1[r - c + (n-1)] = diag2[r+c] = True
            
                # recur to place the next queen
                backtrack(r+1)

                # backtrack and remove the queen
                board[r] = -1
                cols[c] = diag1[r - c + n-1] = diag2[r+c] = False

    backtrack(0)
    return res

print(n_queens(grid))