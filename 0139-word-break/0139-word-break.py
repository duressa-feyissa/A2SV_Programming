class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        memory = {}
        def dp(index):
            if index >= N:
                return True
            if index in memory:
                return memory[index]
            for word in wordDict:
                if word == s[index: len(word) +index]:
                    if dp(index + len(word)):
                        memory[index] = True
                        return True
            memory[index] = False
            return False
        return dp(0)
                        
                        
            
        