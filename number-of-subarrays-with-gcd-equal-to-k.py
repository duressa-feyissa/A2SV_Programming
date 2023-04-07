class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        count = 0 
        n = len(nums)
        for i in range(n):
            if nums[i] % k:
                continue
            gcf = nums[i]
            for j in range(i, n):
                if nums[j] % k == 0:
                    gcf = gcd(gcf, nums[j])
                    if gcf == k:
                        count += 1
                else:
                    break
        return count