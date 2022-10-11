class Solution:
    def calculate(self, s: str) -> int:
        i = 0
        flag = 0
        new = []
        tmp = ""
        while i < len(s):
            if s[i] in " +-*/":
                if s[i] != " ":
                    new.append(int(tmp))
                    new.append(s[i])
                    tmp = ""
            else:
                tmp += s[i]
            i+=1
        new.append(int(tmp))
        i = 0
        flag = 0
        while i < len(new):
            if new[i] == "/":
                y = new[i-1] // new[i+1]
                flag = 1
            if new[i] == "*":
                y = new[i-1] * new[i+1]
                flag = 1
            if flag == 1:
                x = []
                x.append(y)
                new = new[:i-1] + x + new[i+2:]
                flag = 0
                i -= 2
            i+=1
        add = []
        i = 0
        while i < len(new):
            if new[i] == "-":
                new[i+1] *= -1
            if new[i] != "+" and new[i] != "-":
                add.append(new[i])
            i += 1
        return sum(add)
