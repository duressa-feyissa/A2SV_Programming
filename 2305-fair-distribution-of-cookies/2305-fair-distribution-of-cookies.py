class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        ans = float('inf')
        bags = [0]*k
        bags[0] += cookies[0]
        
        def backTrack(i, n):
            nonlocal ans

            if n == i:
                ans = min(ans, max(bags))
                return

            for j in range(k):
                bags[j] += cookies[i]
                backTrack(i + 1, n)
                bags[j] -= cookies[i]
        
        backTrack(1, len(cookies))
        return ans
