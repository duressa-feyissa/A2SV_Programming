class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        stack = []
        n = len(height)
        
        for i in range(n):
            
            while stack and height[stack[-1]] < height[i]:
                popped = stack.pop()
                if stack:
                    Min = min(height[stack[-1]], height[i])
                    cal = (Min - height[popped]) * (i - stack[-1] - 1)
                    count += cal
            stack.append(i)
        
        return count