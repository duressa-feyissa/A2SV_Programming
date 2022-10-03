class Solution:
    def isValid(self, s: str) -> bool:
        Mark1 = "({["
        Mark2 = ")}]"
        hold = ""
        count = [0,0,0]
        for i in s:
            if i in Mark1:
                hold += i
                count[Mark1.index(i)] += 1
            if i in Mark2:
                if count[Mark2.index(i)] != 0:
                    if Mark1.index(hold[-1]) == Mark2.index(i):
                        count[Mark2.index(i)] -= 1
                        hold = hold[:-1]
                else:
                    return False
        if sum(count) == 0:
            return True
        return False
      
