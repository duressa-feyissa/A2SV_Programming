class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        new_list = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] == target:
                new_list.append(i)
        return new_list
        
