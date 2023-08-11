class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        memory = [1] * N
        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    memory[i] = max(memory[i], memory[j] + 1)
        return max(memory)
