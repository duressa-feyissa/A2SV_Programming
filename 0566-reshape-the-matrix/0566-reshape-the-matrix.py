class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        rows = len(mat)
        colums = len(mat[0])
        if rows * colums != r * c:
            return mat                
        
        left = 0
        temp = []
        result = []
        for row in range(rows):
            for col in range(colums):
                temp.append(mat[row][col])
                if left < c - 1:
                    left += 1
                else:
                    left = 0
                    result.append(temp)
                    temp = []
        return result
                    
        
        