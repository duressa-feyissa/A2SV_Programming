class Solution:
    def convert(self, s: str, numRows: int) -> str:
        col = 0
        i=0
        while i < len(s):
            col += 1
            i += numRows
            j = numRows - 2
            while j > 0:
                col += 1
                j -= 1
                i += 1
                
        if numRows == 1:
            return s         
        matrix = [[0 for i in range(col)] for _ in range(numRows)]
        right = 0
        i = 0

        while i < len(s):
            top = 0   
            while top < numRows and i < len(s):
                matrix[top][right] = s[i]
                i+=1
                top+=1
            right += 1
            down = numRows - 2
            while down > 0 and i < len(s):
                matrix[down][right] = s[i]
                i += 1
                down -= 1
                right += 1
                
        answer = ""
        for i in range(numRows):
            for j in range(right):
                if matrix[i][j] != 0:
                    answer += matrix[i][j]
        
        return answer
        
            
            
            
        