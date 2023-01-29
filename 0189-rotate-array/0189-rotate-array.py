class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        array = nums.copy()
        left = 0
        right = -k
        while left < n:
            nums[left] = array[right]
            left+=1
            right+=1
                