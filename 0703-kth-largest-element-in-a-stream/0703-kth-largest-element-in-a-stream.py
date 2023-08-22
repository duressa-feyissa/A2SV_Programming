class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.array = nums
        heapify(self.array)
        self.k = k
        N = len(self.array)
        for _ in range(N - self.k):
            heappop(self.array)

    def add(self, val: int) -> int:
        if len(self.array) >= self.k:
            heappushpop(self.array, val)
        else:
            heappush(self.array, val)
        return self.array[0]