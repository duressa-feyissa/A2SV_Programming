class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        target = 0
        for num in nums:
            target |= num
        n = len(nums)
        count = 0
        array = []
    
        for i in range(2 ** n):
            j = i
            OR = 0
            index = 0
            while j:
                if j & 1:
                    array.append(nums[index])
                    OR |= nums[index]
                j = j >> 1                    
                index += 1
            if OR == target:
                count += 1
                
        return count