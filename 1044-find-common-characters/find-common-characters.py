from collections import Counter
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        check = [0] * 26
        offset = ord('a')
        for char in words[0]:
            check[ord(char) - offset] += 1        
        for word in words:
            fre = Counter(word)
            for index in range(len(check)):
                check[index] = min(fre[chr(index + offset)], check[index])
                
        answer = []
        for val in range(len(check)):
            if check[val] != 0:
                answer.extend([chr(val + offset)] * check[val])
        return answer
                
            
        