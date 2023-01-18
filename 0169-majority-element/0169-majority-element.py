class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        frequency = Counter(nums)
        values = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        return values[0][0]
        