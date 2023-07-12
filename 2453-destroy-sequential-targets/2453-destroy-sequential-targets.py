class Solution:
    def destroyTargets(self, nums: List[int], space: int) -> int:
        N = len(nums)
        nums.sort()
        counter = Counter()
        for i in range(N):
            counter[nums[i] % space] += 1
        Max = 0
        val = 0
        for i in range(N):
            if Max < counter[nums[i] % space]:
                Max = counter[nums[i] % space]
                val = nums[i]
        return val
            