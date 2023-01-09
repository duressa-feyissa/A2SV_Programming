class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        length = len(words)
        Maximum = float('-inf')
        
        for word in words:
            Maximum = max(Maximum, len(word))
        answer = []
        
        for index in range(Maximum):
            string = ""
            for word in words:
                if index < len(word):
                    string += word[index]
                else:
                    string += " "
            answer.append(string.rstrip())
        return answer
                    
            
        
        