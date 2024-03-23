
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        N = len(keys)
        
        dp = [0] * (N + 2) 
        
        for i in range(N - 1, -1, -1):
            if i < N - 1 and keys[i] + 1 == keys[i + 1]:
                dp[i] = max(counter[keys[i]] * keys[i] + dp[i + 2], dp[i + 1])
            else:
                dp[i] = counter[keys[i]] * keys[i] + dp[i + 1]
        
        return dp[0]
