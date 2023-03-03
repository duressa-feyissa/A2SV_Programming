class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0] = 1
        total = 0
        ans = 0
        
        for num in nums:
            total += num
            sub = total - goal
            ans += hash_map[sub]
            hash_map[total] += 1
        
        return ans