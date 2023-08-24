class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        N = len(s)
        answer = []
        def backTrack(index, path):
            if index >= N:
                answer.append(" ".join(path[:]))
                return
            for word in wordDict:
                if word == s[index: len(word) + index]:
                    path.append(word)
                    temp = backTrack(index + len(word), path)
                    path.pop()
                    
        backTrack(0, [])
        
        return answer
                    
        
        
        