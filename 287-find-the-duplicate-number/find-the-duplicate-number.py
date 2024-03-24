class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bit_vector = 0
        
        for num in nums:
            bit_mask = 1 << (num - 1)
            if bit_vector & bit_mask:
                return num
            bit_vector |= bit_mask
