class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        counter = Counter(nums)
        keys = sorted(counter.keys())
        N = len(keys)
        memo = {}
        def dp(index):
            if index > N - 1:
                return 0
            if index in memo:
                return memo[index]
            if index < N - 1 and keys[index] + 1 == keys[index + 1]:
                memo[index] = max(dp(index + 1), counter[keys[index]] * keys[index] + dp(index + 2))
            else:
                memo[index] = counter[keys[index]] * keys[index] + dp(index + 1)
            return memo[index]
        return dp(0)