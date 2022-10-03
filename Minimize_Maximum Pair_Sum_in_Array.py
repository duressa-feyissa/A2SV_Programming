class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        new1 = sorted(nums, reverse=True)
        new2 = sorted(nums)
        new = [new1[i] + new2[i] for i in range(len(nums)//2)]
        return max(new)
      
