class Solution:
    def numDecodings(self, s: str) -> int:
        memory = {}
        N = len(s)
        def dp(i):
            if i == N:
                return 1
            if i > N:
                return 0
            if i not in memory:
                count = 0
                if s[i] != "0":
                    count += dp(i + 1)
                else:
                    return 0
                if int(s[i: i+2]) < 27:
                    count += dp(i + 2)
                memory[i] = count 
            return memory[i] 
        return dp(0)
        