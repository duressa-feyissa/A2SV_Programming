class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        hash_map = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if row - col in hash_map:
                    if matrix[row][col] != hash_map[row - col]:
                        return False
                else:
                    hash_map[row - col] = matrix[row][col]
        return True
                        
                
                
            
        
        
        
        
        