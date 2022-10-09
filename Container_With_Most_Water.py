class Solution:
    def maxArea(self, height: List[int]) -> int:
        Max = -1
        i = 0
        j = len(height) - 1
        while i < j:
            x = j - i
            y = min(height[i], height[j])
            if x * y > Max:
                Max = x * y
            if height[i] > height[j]:
                j -= 1
            elif height[i] < height[j]: 
                i += 1
            else:
                i += 1
                j -= 1
        return Max
   
