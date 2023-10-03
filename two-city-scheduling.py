class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        array = []
        for i in range(len(costs)):
            array.append((costs[i][0] - costs[i][1], i))
        array.sort()
        ans = 0
        for i in range(len(costs) // 2):
            ans += costs[array[i][1]][0]
        for i in range(len(costs) // 2, len(costs)):
            ans += costs[array[i][1]][1]
        return ans