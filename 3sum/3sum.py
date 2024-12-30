from collections import defaultdict
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        checker = {}
        for index, num in enumerate(nums):
            checker[num]=index

        N = len(nums)
        answer = set()

        for i in range(N):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, N):
                target = -(nums[i] + nums[j])
                if target in checker:
                    k = checker[target]
                    if i != k and j != k:
                        temp = tuple(sorted((nums[k], nums[i], nums[j])))
                        if temp not in answer:                            
                            answer.add(temp)
                   

        return [list(triplet) for triplet in answer]
                    
                    
                
        