class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map = {0 : 1}
        total = 0
        ans = 0
        for num in nums:
            total += num
            ans += hash_map.get(total % k, 0)
            hash_map[total % k] = hash_map.get(total % k, 0) + 1   
        return ans
        

        