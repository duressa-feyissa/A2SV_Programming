class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        grid = list(map(sorted, grid))
        grid = list(zip(*grid))
        return sum(list(map(max,grid)))
        
        