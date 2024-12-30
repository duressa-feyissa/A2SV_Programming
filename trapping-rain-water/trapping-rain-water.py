class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        N = len(height)
        
        for i in range(N):
            while stack and height[stack[-1]] < height[i]:
                poppedIndex = stack.pop()
                if stack:
                    water_height = min(height[stack[-1]], height[i]) - height[poppedIndex]
                    width = i - stack[-1] - 1
                    ans += water_height * width
            
            stack.append(i)
        
        return ans
