class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        Max = -1
        stack = []
        hold = 0
        i, j, count= 0, 0, 0
        while j < len(nums): 
            if k == 0:
                count = 0
                while j < len(nums):
                    if nums[j] == 0:
                        break
                    j+=1
                    count+=1
                Max = max(Max, count)
                j+=1
            elif nums[j] == 1:
                j += 1
                if j >= len(nums):
                    Max = max(Max, j - i)
            else:
                stack.append(j)
                count+=1
                j+=1
                if j >= len(nums):
                    Max = max(Max, j - i)
            while count == k and j < len(nums) and k != 0:
                if nums[j] == 1:
                    j+=1
                    if j >= len(nums):
                        Max = max(Max, j - i)
                else:
                    Max = max(Max, j - i)
                    i = stack[len(stack)-k] + 1
                    count -= 1 
        return Max
                
                
        
