class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[List[int]]:
        N = len(nums)
        ans = []
        
        if N == 0:
            return [[lower, upper]]
        
        if lower < nums[0]:
            ans.append([lower, nums[0] - 1])
        
        for i in range(N - 1):
            if nums[i] + 1 < nums[i + 1]:
                ans.append([nums[i] + 1, nums[i + 1] - 1])
        
        if upper > nums[-1]:
            ans.append([nums[-1] + 1, upper])
        
        return ans