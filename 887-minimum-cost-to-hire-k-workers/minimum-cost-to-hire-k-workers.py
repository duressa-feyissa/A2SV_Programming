class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans = float('inf')
        heap=[]
        sum_q=0
        for (w,q) in sorted((w/q,q) for w,q in zip(wage, quality)):
            if len(heap) == k:
                sum_q+=heappop(heap)
            sum_q+=q
            heappush(heap,-q)
            if len(heap) == k:
                ans = min(ans,sum_q*w)    
        return ans        

                   