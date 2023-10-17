class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        M, N = len(houses), len(heaters)
        answer = 0
        for i in range(M):
            index = bisect_right(heaters, houses[i])
            if index < N:
                result = min(abs(heaters[index] - houses[i]), abs(heaters[index - 1] - houses[i]))
                answer = max(answer, result)
            else:
                answer = max(answer,abs(heaters[index - 1] - houses[i]))

        return answer