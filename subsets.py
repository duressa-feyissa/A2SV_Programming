class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []
        n = len(nums)
        
        def backTrack(i, subset):
            answer.append(subset[:])
            
            if i == n:
                return
            
            for j in range(i,n):
                subset.append(nums[j])
                backTrack(j + 1, subset)
                subset.pop()
        
        backTrack(0,[])
        
        return answer