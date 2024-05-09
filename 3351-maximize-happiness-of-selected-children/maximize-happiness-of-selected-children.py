class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        happinessScore = 0

        for turn, score in enumerate(happiness):
            if k == turn:
                return happinessScore
            happinessScore += max(0, score - turn)

        return happinessScore