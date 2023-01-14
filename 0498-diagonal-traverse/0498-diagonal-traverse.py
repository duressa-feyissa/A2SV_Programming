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