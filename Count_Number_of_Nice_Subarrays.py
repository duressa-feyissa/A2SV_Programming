class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        count = 0
        add = 0
        new = {0:1}
        for i in nums:
            add += i
            sub = add - k
            count+=new.get(sub,0)
            new[add] = 1 + new.get(add,0)
        return count
