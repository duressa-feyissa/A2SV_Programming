class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operator = ["+","-","*","/"]
        i = 0
        nums = len(tokens)
        while i < nums:
            if tokens[i] in operator:
                a = int(tokens[i - 1])
                b = int(tokens[i - 2])
                if tokens[i] == operator[0]:
                    value = a + b
                elif tokens[i] == operator[1]:
                    value = b - a
                elif tokens[i] == operator[2]:
                    value = a * b
                else:
                    value = b / a
                new1 = tokens[:i-2] + [value] 
                new2 = tokens[i+1:]
                tokens = new1 + new2
                i -= 3
                nums = len(tokens)
            i += 1
        return sum(list(map(int, tokens)))
            
        
        
