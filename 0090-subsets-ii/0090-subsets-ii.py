class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        answer = set()
        nums.sort()
        n = len(nums)
        
        def backTrack(i, subset):
            temp = tuple(subset)
            
            if temp not in answer:
                answer.add(temp)
            else:
                return
            
            if i == n:
                return
            
            for j in range(i,n):
                subset.append(nums[j])
                backTrack(j + 1, subset)
                subset.pop()
        
        backTrack(0,[])
        
        return list(map(list, answer))
        