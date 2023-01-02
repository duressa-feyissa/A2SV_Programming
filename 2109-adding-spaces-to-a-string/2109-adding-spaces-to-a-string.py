class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        
        left = 0
        answer = ""
        for i in range(len(s)):
            if left < len(spaces) and spaces[left] == i:
                answer += " "
                answer += s[i]
                left +=1
            else:
                answer+=s[i]
        return answer
                
        