class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        check = set()
        answer = [0,0]
        array = set(nums)
        for index in range(len(nums)):
            if index + 1 not in array:
                answer[1] = index + 1
            if nums[index] in check:
                answer[0] = nums[index]
            check.add(nums[index])
        return answer
            
                
            
        