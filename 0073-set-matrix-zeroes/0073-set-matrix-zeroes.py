class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #without using any extra space == O(1)
        flag = False       
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    if i == 0 and j == 0:
                        flag = True
                    else:
                        if i != 0 and j == 0 and matrix[0][0] == "r":
                            flag = True
                        matrix[0][j] = "c"
                        matrix[i][0] = "r"
                        
        #make columns zero
        for j in range(len(matrix[0])):
            if matrix[0][j] == "c" or (j == 0 and flag):
                for i in range(len(matrix)):
                    if matrix[i][j] != 'r':
                        matrix[i][j] = 0
                    
        #make rows zero
        for i in range(len(matrix)):
            if matrix[i][0] == "r" or (i == 0 and flag):
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0

        
                        
        
        
                
        
