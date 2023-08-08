class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        N = len(requests)
        def backTrack(index, path):
            count = len(path)
            check = Counter()
            for x, y in path:
                check[x] -= 1
                check[y] += 1
            for val in list(check.values()):
                if val != 0:
                    count = 0
            for j in range(index, N):
                path.append(requests[j])
                count = max(count, backTrack(j + 1, path))
                path.pop()
            return count
        return backTrack(0, [])
            
            
        