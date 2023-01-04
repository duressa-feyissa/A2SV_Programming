class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        check = matrix[0][0]
        for row in range(len(matrix)): 
            for col in range(len(matrix[0])):
                if row == 0 and matrix[row][col] == 0:
                    check = 0
                if row != 0 and matrix[row][col] == 0:
                    matrix[row][0] = 0
                    matrix[0][col] = 0
        for row in range(len(matrix) - 1, 0, -1):
            if matrix[row][0] == 0:
                for col in range(len(matrix[0])):
                    matrix[row][col] = 0
            else:
                for col in range(len(matrix[0])):
                    if matrix[0][col] == 0:
                        matrix[row][col] = 0
        if check == 0:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
            
                
                
        
       