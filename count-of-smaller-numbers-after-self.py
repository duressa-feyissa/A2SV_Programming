class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        def mergeSort(nums, left, right):
            if left == right:
                return [nums[left]]
            middle = (left + right) // 2
            leftSide = mergeSort(nums, left, middle)
            rightSide = mergeSort(nums, middle + 1, right)
            length = len(rightSide)                
            for i in range(left, middle + 1):
                answer[i] += bisect_left(rightSide, nums[i])
            return self.merge(leftSide, rightSide)
        mergeSort(nums, 0, len(nums) - 1)
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