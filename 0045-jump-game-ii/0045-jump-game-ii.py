class Solution:
    def jump(self, nums: List[int]) -> int:
        memory = {}
        N = len(nums)
        def dp(index):
            if index >= N - 1:
                return 0
            if nums[index] + index >= N - 1:
                memory[index] = 1
                return memory[index]
            if index in memory:
                return memory[index]
            Min = N
            for i in range(index + 1, min(index + 1 + nums[index], N + 1)):
                Min = min(dp(i) + 1, Min)
            memory[index] = Min
            return memory[index]
        return dp(0)
                
                
        