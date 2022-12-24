class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        remove = nums.count(val)
        hold = nums.count(val)
        left = 0
        count = 0
        LENGTH = len(nums)
        while left + count < LENGTH:
            while left + count < LENGTH and remove != 0:
                if nums[left + count] == val:
                    count += 1
                    remove-=1
                else:
                    break           
            if left + count < LENGTH:
                nums[left] = nums[left + count]
            left += 1
        hold = LENGTH - hold
        while hold != len(nums):
            nums.pop()