class Solution:
    def sortSentence(self, s: str) -> str:
        lst = list(s.split(" "))
        new = lst.copy()
        for i in range(len(lst)):
            num = len(lst[i])
            string = str(lst[i])
            index = int(string[-1:])
            new[index - 1] = string[0:num-1]
        return " ".join(new)
        
