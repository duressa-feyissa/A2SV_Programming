class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        arrayHash = {}
        for index, value in enumerate(score):
            arrayHash[value] = index
        keys = sorted(arrayHash.keys(), reverse=True)
        answer = [0] * len(score)
        for index, value in enumerate(keys):
            if index + 1 == 1:
                answer[arrayHash[value]] = "Gold Medal"
            elif index + 1 == 2:
                answer[arrayHash[value]] = "Silver Medal"
            elif index + 1 == 3:
                answer[arrayHash[value]] = "Bronze Medal"
            else:
                answer[arrayHash[value]] = str(index + 1)
        return answer
                
                
                
            