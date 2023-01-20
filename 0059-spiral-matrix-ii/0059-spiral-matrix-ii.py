class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        top = 0 #|v
        right = n - 1 # <-
        left = 0 # ->
        bottom = n - 1# ^|
        matrix = [list(range(n)) for _ in range(n)]
        
        count = 1
        while top < bottom and left < right:
            #top
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            top += 1
            
            #right
            for i in range(top - 1, bottom):
                matrix[i][right] = count
                count += 1
            right -= 1
            
            #bottom
            for i in range(right + 1, left, -1):
                matrix[bottom][i] = count
                count += 1
            bottom -= 1
            
            #left
            for i in range(bottom + 1, top - 1, -1):
                matrix[i][left] = count
                count += 1
            left += 1
        if n % 2:
            matrix[top][left] = count
        return matrix         
            
            
            
            
        
        
        