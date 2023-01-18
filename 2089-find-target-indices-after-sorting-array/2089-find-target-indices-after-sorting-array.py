class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        new_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                new_list.append(i)
        return new_list    