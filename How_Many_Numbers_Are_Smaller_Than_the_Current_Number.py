class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        new_list = []
        for i in range(len(nums)):
            count = 0 
            for j in range(len(nums)):
                if j != i and nums[j] < nums[i]:
                    count += 1
            new_list.append(count)
        return new_list
