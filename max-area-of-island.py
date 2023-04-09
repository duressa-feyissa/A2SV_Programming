class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[-1,0], [1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])
        visited = [[0 for _ in range(COLS)] for _ in range(ROWS)]

        def inbound(r, c):
            return 0 <= r < ROWS and 0 <= c < COLS
        def dfs(row, col):
            area = 0
            visited[row][col] = 1
            for x, y in directions:
                r = row + x
                c = col + y
                if inbound(r, c):
                    if visited[r][c] == 0 and grid[r][c]:
                        area += dfs(r, c)
            return area + 1
        Max = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] and visited[i][j] == 0:
                    Max = max(dfs(i, j), Max)
        return Max