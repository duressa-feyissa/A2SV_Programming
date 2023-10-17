class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        N = len(gas)        
        start, add, count = -1, 0, 0
        for i in range(2 * N):
            index = i % N
            diff = gas[index] - cost[index]
            if diff > -1 and add == 0:
                start = index
            add += diff
            if count == N:
                return start
            if add < 0:
                add = 0
                count = 0
            else:
                count += 1  
        return -1