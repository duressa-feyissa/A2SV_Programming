class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k = n - k

        def quickSort(l=0, r=n-1):
            p, pivot = l, nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1

            nums[p], nums[r] = pivot, nums[p]

            if k > p:
                return quickSort(p + 1, r)
            elif k < p:
                return quickSort(l, p - 1)
            return nums[k]

        return quickSort()