class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        answer = []
    
        def backtrack(permutation, check):
            
            if len(permutation) == n:
                answer.append(permutation[:])
                return
            
            for j in range(n):
                if not ((1 << j) & check):
                    check = 1 << j | check
                    permutation.append(nums[j])
                    backtrack(permutation, check)
                    permutation.pop()
                    check = check ^ (1 << j)
        backtrack([], 0)
        return answer