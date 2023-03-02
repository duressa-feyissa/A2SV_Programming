class Solution:
    def decodeString(self, s: str) -> str:
        return self.solve(s)[0]
    
    def solve(self, s):
        digit = ""
        char = ""
    
        if s == "":
            return ["", ""]
        
        if s[0] == "]":
            return ["", s[1:]]

        while s and s[0].isdigit():
            digit += s[0]
            s = s[1:]

        substrings = self.solve(s[1:])
        
        if s and s[0] != "[":
            char = s[0] + substrings[0]
        else:
            char = substrings[0]
        if digit:
            temp = self.solve(substrings[1])
            return [(int(digit) * char) + temp[0], temp[1]] 

        return [char, substrings[1]]