class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        #create matrix with a row + 1 and col + 1 
        matrix = [[0 for _ in range(cols + 1)] for _ in range(rows + 1)]
        
        #make last column of matrix infinity
        for i in range(rows):
            matrix[i][cols] = float('inf')
            
        #make last row of matrix infinity
        for i in range(cols):
            matrix[rows][i] = float('inf')
        matrix[rows][cols-1] = 0

        for i in range(rows - 1, -1, -1):
            for j in range(cols - 1, -1, -1):
                matrix[i][j] = grid[i][j] + min(matrix[i][j+1], matrix[i+1][j])        
                
        return matrix[0][0]
        
        
        
        