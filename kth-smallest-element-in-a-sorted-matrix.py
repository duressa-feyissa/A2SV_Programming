class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        array = []
        N = len(matrix)
        count = 0
        for row in range(N):
            for col in range(N):
                heappush(array, matrix[row][col])
        for _ in range(k - 1):
            heappop(array)
        return array[0]