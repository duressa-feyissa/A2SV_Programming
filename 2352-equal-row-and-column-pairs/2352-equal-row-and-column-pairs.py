class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        transpose = list(zip(*grid))
        answer = 0
        for row in grid:
            for column in transpose:
                if row == list(column):
                    answer+=1
        return answer
                    