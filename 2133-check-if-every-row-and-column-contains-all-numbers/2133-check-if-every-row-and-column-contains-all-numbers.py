class Solution:
    def checkValid(self, matrix: List[List[int]]) -> bool:
        n = len(matrix)
        check = list(range(1,n+1))
        trans = list(zip(*matrix))
        for index in range(n):
            if sorted(matrix[index]) != check or sorted(trans[index]) != check:
                return False
        return True
        
        
        