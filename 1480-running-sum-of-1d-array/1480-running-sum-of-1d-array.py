class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        total = 0
        for num in nums:
            total += num
            ans.append(total)
        return ans