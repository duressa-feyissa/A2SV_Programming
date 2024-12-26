class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        R, C = len(grid), len(grid[0])
        count = 0
        visited = set()
        
        def inBound(r, c):
            return 0 <= r < R and 0 <= c < C
        
        def dfs(r, c): 
            visited.add((r,c))
            for x, y in dirs:
                nx = x + r
                ny = y + c
                if inBound(nx, ny) and (nx, ny) not in visited and grid[nx][ny] == '1':
                    dfs(nx, ny)
                    
        for x in range(R):
            for y in range(C):
                if (x,y) not in visited and grid[x][y] == '1':
                    dfs(x,y)
                    count += 1
        
        return count
                    
            
        
        
        