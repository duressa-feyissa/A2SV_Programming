class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        
        stack = []
        n = len(nums)
        answer = [-1] * n
        
        for i in range(2 * n - 1):
            
            while stack and nums[stack[-1]] < nums[i % n]:
                popped = stack.pop()
                answer[popped] = nums[i % n]
            
            stack.append(i % n)
        
        return answer