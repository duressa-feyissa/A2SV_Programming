class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = set()
        nums.sort()
    
        def backtrack(i, permutation):
            
            if len(permutation) == n:
                check = tuple(permutation)
                if check not in answer:
                    answer.add(check)
                return
            
            for j in range(n):
                if nums[j] not in permutation:
                    permutation.append(nums[j])
                    backtrack(j, permutation)
                    permutation.pop()
                    
        backtrack(0, [])
        
        return answer
"""     
            [1]         []
            [1, 2]      [1]
            [1, 2, 3]   [1, 2]
            
            [1]         []
            [1, 3]      [1]
           [1, 3, 2]   [1, 3]
"""
            
    
    
    
    
    
    
    
    



    
    