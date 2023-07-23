class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N = len(nums)
        memory = defaultdict(int)
        for i in range(N):
            check = set()
            for j in range(i+1, N):
                if nums[j] not in check:
                    diff = nums[j] - nums[i]
                    memory[(nums[j], diff)] = memory[(nums[i], diff)] + 1
                check.add(nums[j])
        return max(list(memory.values())) + 1