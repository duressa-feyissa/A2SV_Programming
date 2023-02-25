from operator import add, sub, mul, floordiv
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:    
        stack = []
        operation = {"+": add, "-": sub, "*": mul, "/": truediv}
        
        for token in tokens:
            if token in operation:
                a = stack.pop()
                b = stack.pop()
                c = operation[token](b, a)
                stack.append(int(c))
            else:
                stack.append(int(token))
        return stack[0]