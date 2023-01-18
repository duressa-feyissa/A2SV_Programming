class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        answer = []
        for i in range(0,len(nums) - 2):
            current = i
            left = i + 1
            right = length-1
            if i > 0 and nums[current] == nums[current-1]:
                continue
            while left < right:
                total = nums[current] + nums[left] + nums[right]
                if total == 0:
                    answer.append([nums[current], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while nums[left] == nums[left-1] and left < right:
                        left+=1
                    while nums[right] == nums[right+1] and left < right:
                        right-=1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return answer
                    
        
        
        
        
        