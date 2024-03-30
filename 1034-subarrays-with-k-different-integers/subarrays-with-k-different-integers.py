class Solution:
    def solve(self, nums, k):
        n = len(nums)
        ans = 0
        mpp = {}
        i = j = 0
        while j < n:
            mpp[nums[j]] = mpp.get(nums[j], 0) + 1
            while len(mpp) > k:
                mpp[nums[i]] -= 1
                if mpp[nums[i]] == 0:
                    del mpp[nums[i]]
                i += 1
            ans += j - i + 1
            j += 1
        return ans

    def subarraysWithKDistinct(self, nums, k):
        return self.solve(nums, k) - self.solve(nums, k - 1)