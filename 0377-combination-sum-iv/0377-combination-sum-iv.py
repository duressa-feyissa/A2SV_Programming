class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memory = {}
        nums.sort()
        N = len(nums)
        def dp(index, add):
            state = (index, add)
            if state not in memory:
                if add == target:
                    return 1
                count = 0
                for i in range(N):
                    if add + nums[i] > target:
                        break
                    count += dp(i, add + nums[i])
                memory[state] = count
            return memory[state]
        return dp(0,0)
        
        
        
        