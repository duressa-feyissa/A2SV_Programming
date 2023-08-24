class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        answer = []
        memory = {}
        def dp(index):
            if index >= N:
                return []
            result = []
            for word in wordDict:
                if word == s[index: len(word) + index]:
                    temp = dp(index + len(word))
                    if temp:
                        for array in temp:
                            array.append(word)
                            result.append(array)
                    else:
                        result.append([word])
            return result
        for array in dp(0):
            if N == sum(list(map(lambda x: len(x), array))):
                answer.append(" ".join(array[::-1]))
        return answer
                    
        
        
        