class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        character = [chr(i) for i in range(97, 123)]
        array = [0] * (n + 1)
        for start, end, direction in shifts:
            operation = 1
            if direction == 0:
                operation = - 1
            array[start] += operation
            array[end + 1] -= operation

        prefix = 0
        result = ""
        for i in range(n):
            prefix += array[i]
            index = (ord(s[i]) + prefix - 97) % 26
            result += character[index]
        
        return result
            
        
            
        
        