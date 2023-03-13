class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = set()
        nums.sort()
    
        def backtrack(permutation):
            
            if len(permutation) == n:
                check = tuple(permutation)
                if check not in answer:
                    answer.add(check)
                return
            
            for j in range(n):
                if nums[j] not in permutation:
                    permutation.append(nums[j])
                    backtrack(permutation)
                    permutation.pop()
                    
        backtrack([])
        
        return answer

            
    
    
    
    
    
    
    
    



    
    