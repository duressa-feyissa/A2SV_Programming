class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        array = []
        for pile in piles:
            heappush(array, -pile)
        for _ in range(k):
            if array:
                popped = -heappop(array)
                remain = popped - (popped // 2)
                heappush(array, -remain)
        return -sum(array)