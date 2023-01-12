from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = Counter(words[0])
        answer = []
        for index in range(1,len(words)):
            word = Counter(words[index])
            for key in check.keys():
                if key in word:
                    check[key] = min(check[key], word[key])
                else:
                    check[key] = -1
        
        for key, value in check.items():
            if value != -1:
                for i in range(value):
                    answer.append(key)
        
        return answer
                
            
        