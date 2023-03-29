class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        array = [-1] * (n + 1)
        for num in nums:
            array[num] = num
        print(array)
        return array.index(-1)