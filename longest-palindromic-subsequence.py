class Solution:
    def longestPalindromeSubseq(self, s: str) -> int: 
        memory = {}
        def dp(left, right):
            if left > right:
                return 0
            state = (left, right)
            if state in memory:
                return memory[state]
            result = 0
            if s[left] != s[right]:
                result = max(dp(left + 1, right), dp(left, right - 1))
            else:
                if left == right:
                    result = 1
                else:
                    result = dp(left + 1, right - 1) + 2
            memory[state] = result
            return result
        return dp(0, len(s) -1)