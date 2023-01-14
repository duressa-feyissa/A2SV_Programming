class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        count = 0
        m = len(mat)
        n = len(mat[0])
        top = 0
        left = 0
        right= 0
        down = 0
        answer = []
        while count < m * n:           
            #increase
            i = down
            j = left
            while (i >= top and j <= right):
                answer.append(mat[i][j])
                count += 1
                i -= 1
                j += 1
            if right == n - 1:
                top += 1
            if down == m - 1:
                left += 1 
            if right < n - 1:
                right += 1
            if down < m - 1:
                down += 1
            
            #decrease
            i = top
            j = right
            while (i <= down and j >= left):
                answer.append(mat[i][j])
                count += 1
                i += 1
                j -= 1
            if right == n - 1:
                top += 1
            if down == m - 1:
                left += 1
            if right < n - 1:
                right += 1
            if down < m - 1:
                down += 1 
        return answer
"""
#methed 2: using map but less efficient
from collections import defaultdict
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonal = defaultdict(list)
        answer = []
        
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                diagonal[row + col].append((row,col))
        
        for key in sorted(diagonal.keys()):
            if key % 2 == 0:
                temp = sorted(diagonal[key], reverse=True)
            else:
                temp = diagonal[key]
            for item in temp:
                answer.append(mat[item[0]][item[1]])
        return answer
"""