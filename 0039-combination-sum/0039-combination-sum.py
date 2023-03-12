class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = set()
        n = len(candidates)
        candidates.sort()
        
        def backTrack(i, candidate):
            
            _sum = sum(candidate)
            if _sum == target :
                check = tuple(candidate[:])
                if check not in answer: 
                    answer.add(check)
                return
            
            if n == i or _sum > target:
                return
            
            for j in range(i, n):
                candidate.append(candidates[j])
                backTrack(j, candidate)
                candidate.pop()
        
        backTrack(0, [])
            
        return answer
        
        
        
        
        
        