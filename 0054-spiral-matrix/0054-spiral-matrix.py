class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        answer = []
        total = m * n
        top = 0
        left = 0
        right = n
        bottom = m
        if n == 1:
            return [i[0] for i in matrix]
        while count < total:    
            for i in range(left,right):
                answer.append(matrix[top][i])
            top+=1
            for i in range(top,bottom-1):
                answer.append(matrix[i][right-1])
            right-=1
            if top == bottom:
                break
            for i in range(right,left-1,-1):
                answer.append(matrix[bottom-1][i])
            bottom-=1
            if left == right:
                break
            for i in range(bottom-1,top-1,-1):
                answer.append(matrix[i][left])
            count = len(answer)
            left+=1
        return answer
        