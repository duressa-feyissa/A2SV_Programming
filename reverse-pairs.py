class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        answer = 0
        def mergeSort(nums):
            nonlocal answer
            left, right = 0, len(nums)
            if left + 1 == right:
                return [nums[left]]
            middle = (left + right) // 2
            leftSide = mergeSort(nums[left: middle])
            rightSide = mergeSort(nums[middle: right])
            length = len(rightSide)
            
            for i in range(len(leftSide) - 1, -1, -1):
                position = bisect_left(rightSide, leftSide[i] / 2)
                if position == 0:
                    break
                else:
                    answer += position

            return self.merge(leftSide, rightSide)
        mergeSort(nums)
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
