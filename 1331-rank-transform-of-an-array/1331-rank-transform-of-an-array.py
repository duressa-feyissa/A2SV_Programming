class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = {}
        count = 1
        for item in sorted(set(arr)):
            rank[item] = count
            count += 1
        answer = []
        for item in arr:
            answer.append(rank[item])
        return answer
        
        
        