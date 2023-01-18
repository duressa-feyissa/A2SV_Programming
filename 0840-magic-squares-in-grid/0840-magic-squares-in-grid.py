class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        top = 0
        left = 0
        count = 0
        while top <= len(grid) - 3:
            while left <= len(grid[0]) - 3:
                count += Solution.checker(self, grid, top, left)
                left += 1
            left = 0
            top += 1
        return count
    
    def checker(self, matrix, top, left) -> int:
        #check elements
        magic = set([i for i in range(1, 10)])
        temp = set()
        for i in range(top, top+3):
            for j in range(left, left+3):
                temp.add(matrix[i][j])
        if magic != temp:#to check if elements are distinct
            return 0
        #add each row
        r1 = matrix[top][left] + matrix[top][left+1] + matrix[top][left+2]
        r2 = matrix[top+1][left] + matrix[top+1][left+1] + matrix[top+1][left+2]
        r3 = matrix[top+2][left] + matrix[top+2][left+1] + matrix[top+2][left+2]
        #add each column
        c1 = matrix[top][left] + matrix[top+1][left] + matrix[top+2][left]
        c2 = matrix[top][left+1] + matrix[top+1][left+1] + matrix[top+2][left+1]
        c3 = matrix[top][left+2] + matrix[top+1][left+2] + matrix[top+2][left+2]
        #add each diagonal
        d1 = matrix[top][left] + matrix[top+1][left+1] + matrix[top+2][left+2]
        d2 = matrix[top+2][left] + matrix[top+1][left+1] + matrix[top][left+2]
        temp = set([r1, r2, r3, c1, c2, c3, d1, d2])
        if len(temp) == 1:
            return 1
        return 0
        
        