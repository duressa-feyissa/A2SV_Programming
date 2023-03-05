class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        
        prefix1 = 0
        perfix2 = 0
        n = len(grid[0])
        total = sum(grid[0])
        robot2Points = float('inf')
        
        for i in range(n):
            prefix1 += grid[0][i]
            surfix = total - prefix1
            robot2Points = min(robot2Points, max(surfix, perfix2))
            perfix2 += grid[1][i]
        return robot2Points