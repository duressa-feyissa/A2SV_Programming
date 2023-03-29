class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        nums = [0] * n
        answer = 0
        for i in range(n):
            nums[i] = nums1[i] - nums2[i]

        def mergeSort(nums, left, right):
            nonlocal answer
            if left == right:
                return [nums[left]]
            middle = (left + right) // 2
            leftSide = mergeSort(nums, left, middle)
            rightSide = mergeSort(nums, middle + 1, right)
            length = len(rightSide)    
            for i in range(left, middle + 1):
                answer += (length - bisect_left(rightSide, nums[i] - diff))
            return self.merge(leftSide, rightSide)
        mergeSort(nums, 0, n - 1)
        return answer
    
    def merge(self, left, right):
        n, m = len(left), len(right)
        pointer1 = 0
        pointer2 = 0
        array = []
        while pointer1 < n and pointer2 < m:
            if left[pointer1] <= right[pointer2]:
                array.append(left[pointer1])
                pointer1 += 1
            else:
                array.append(right[pointer2])
                pointer2 += 1   
        array.extend(left[pointer1:])
        array.extend(right[pointer2:])
        return array