class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        left = 0
        while left < n:
            if nums[left] == left + 1:
                left += 1
            else:
                correctPosition = nums[left] - 1
                if nums[correctPosition] == nums[left]:
                    answer.append(nums[left])
                    left += 1
                elif nums[left] < left + 1:
                    nums[nums[left] - 1] =  nums[left]
                    left += 1                
                else:
                    nums[correctPosition], nums[left] = nums[left], nums[correctPosition]
        return answer 

[4,3,2,7,8,2,3,1]
[7,3,2,4,8,2,3,1]
[3,3,2,4,8,2,7,1]
[2,3,3,4,8,2,7,1]
[3,2,3,4,8,2,7,1]
[3,2,3,4,1,2,7,8]
[3,2,3,4,1,2,7,8]
[1,2,3,4,1,2,7,8]