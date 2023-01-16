class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        columns = len(grid[0])
        left = 0
        top = 0
        temp = []
        result = []
        while left <= columns - 3 and top <= rows - 3:
            largest = 0
            for i in range(top, top + 3):
                for j in range(left, left + 3):
                    largest = max(largest, grid[i][j])
            temp.append(largest)
            if left + 3 < columns:
                left += 1
            else:
                top += 1
                left = 0
                result.append(temp)
                temp = []
        return result    
        
                    
            
        