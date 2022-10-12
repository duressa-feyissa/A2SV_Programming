class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        add = 0
        new = {0:1}
        for i in nums:
            add += i
            sub = add - k
            count+=new.get(sub,0)
            new[add] = 1+new.get(add,0)
        return count
                
        
