class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        N = len(nums)
        M = len(queries)
        prefixSum = [0] * (N + 1)
        for l, r in queries:
            prefixSum[l] += 1
            prefixSum[r+1] -= 1
        for i in range(1,N+1):
            prefixSum[i] = prefixSum[i - 1] + prefixSum[i]
        for i in range(N):
            if nums[i] - prefixSum[i] > 0:
                return False
        return True




        