class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2:
                nums[i] = 1
            else:
                nums[i] = 0
                
        hash_map = {0:1}
        add = 0
        ans = 0
        for i in range(len(nums)):
            add += nums[i]
            ans += hash_map.get(add - k, 0)
            hash_map[add] = 1 + hash_map.get(add, 0)           
        return ans
            
            
            
                
            