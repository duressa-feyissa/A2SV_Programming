class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)
        surfix = []
        total = 1
        for i in range(n - 1, -1, -1):
            total *= nums[i]
            surfix.append(total)
        surfix = surfix[::-1] + [1]

        answer = []
        total = 1
        for i in range(n):
            answer.append(total * surfix[i + 1])
            total *= nums[i]
        
        return answer
        
            
            
            