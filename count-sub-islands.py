class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        directions = [[-1,0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid2), len(grid2[0])

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS

        def dfs(row, col):
            grid2[row][col] = 0
            status = True
            if grid1[row][col] == 0:
                status = False
            for x, y in directions:
                r = row + x
                c = col + y
                if inbound(r, c):
                    if grid2[r][c] == 1:
                        status = dfs(r, c) == True and status 
            return status
    
        count = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1
        return count