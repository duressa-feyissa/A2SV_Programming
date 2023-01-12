class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        cols = len(matrix[0])
        for row in range(len(matrix)):
            if matrix[row][-1] >= target:
                col = cols - 1 
                while col >= 0:
                    if matrix[row][col] == target:
                        return True
                    col -= 1
                return False
        return False
                    