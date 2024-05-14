class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        m, n, ans = len(grid), len(grid[0]), 0

        def dfs(grid, row, col):
            if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] <= 0: return 0
            grid[row][col] = -grid[row][col]

            down = dfs(grid, row+1, col)
            right = dfs(grid, row, col+1)
            up = dfs(grid, row-1, col)
            left = dfs(grid, row, col-1)

            grid[row][col] = -grid[row][col]
            return grid[row][col] + max(max(left, right), max(up, down))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]: ans = max(ans, dfs(grid, i, j))
        return ans