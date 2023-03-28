class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ans = 0
        n = len(nums)
        def quickSort(left, right, n):
            nonlocal ans
            
            if left > right:
                return
            index = left
            pivot = nums[left]
            
            while True:
                while left <= right and pivot >= nums[left]:
                    left += 1
                while left <= right and pivot < nums[right]:
                    right -= 1

                if left <= right:
                    nums[left], nums[right] = nums[right], nums[left]
                else:
                    break

            nums[index], nums[right] = nums[right], nums[index]
            
            if n - k == right:
                ans = nums[right]
                return
            elif right > n - k:
                quickSort(index, right - 1, n)
            else:
                quickSort(right + 1, n - 1, n)    
        quickSort(0, n - 1, n)
        return ans