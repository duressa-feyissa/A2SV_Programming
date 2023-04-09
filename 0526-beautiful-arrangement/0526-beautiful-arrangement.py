class Solution:
    def countArrangement(self, n: int) -> int:
        answer = 0
        def backtrack(permutation, check):
            nonlocal answer
            if len(permutation) == n:
                answer += 1
                return
            
            for j in range(1, n + 1):
                length = len(permutation)
                if not ((1 << j) & check):
                    if (j % (length + 1) == 0) or ((length + 1) % j == 0):
                        check = 1 << j | check
                        permutation.append(j)
                        backtrack(permutation, check)
                        permutation.pop()
                        check = check ^ (1 << j)
        backtrack([], 0)
        return answer
