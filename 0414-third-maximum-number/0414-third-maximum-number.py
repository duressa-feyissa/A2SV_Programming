class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        array = sorted(set(nums), reverse=True)
        if len(array) < 3:
            return array[0]
        return array[2]
        