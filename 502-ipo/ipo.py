from heapq import heapify, heappop, heappush
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        arr = [(c, p) for c, p in zip(capital, profits)]
        arr.sort()

        maxprof = []
        heapify(maxprof)
        cnt, i = 0, 0

        while cnt < k:
            while i < len(profits) and arr[i][0] <= w:
                heappush(maxprof, -arr[i][1])
                i += 1
            
            if maxprof:
                temp = (-heappop(maxprof))
                w += temp
                cnt += 1 
            else:
                return w
        
        return w
