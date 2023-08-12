class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        memory = {}
        def dp(index):
            if index >= N - 1:
                return True
            if index in memory:
                return memory[index]
            if index + nums[index] >= N - 1:
                memory[index] = True
                return True
            stat = False
            for i in range(index + 1, min(N+1, index + nums[index] + 1)):
                stat = stat or dp(i)
            memory[index] = stat
            return stat
        return dp(0)
            
        
                
        
        