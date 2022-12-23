class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:    
        nums.sort(reverse=True)
        ELEMENT = nums[:3]
        left=3
        LENGTH = len(nums)
        if LENGTH == 3:
            if sum(ELEMENT[1:])  > ELEMENT[0]:
                return sum(ELEMENT)
        while left <= LENGTH:
            total = sum(ELEMENT[1:])
            if total > ELEMENT[0]:
                return sum(ELEMENT)
            elif left < LENGTH:
                ELEMENT.remove(ELEMENT[0])
                ELEMENT.append(nums[left])
            left+=1
        return 0
            
                
            
            
