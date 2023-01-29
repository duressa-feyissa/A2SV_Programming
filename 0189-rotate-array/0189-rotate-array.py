class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        #method 1: with space O(1)
        n = len(nums) - 1
        k = k % len(nums)
        #reverse from index 0 to n - k using two pointer
        self.reverseArray(nums, 0, n - k)
        
        #reverse from index n - k to n using two pointer
        self.reverseArray(nums, n - k + 1, n)
        
        #reverse the whole array using two pointer
        self.reverseArray(nums, 0, n)
    
    @staticmethod
    def reverseArray(nums, left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
"""
method = #2
using space O(n)
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
"""
