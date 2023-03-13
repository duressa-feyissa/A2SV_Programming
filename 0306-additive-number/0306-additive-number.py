class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        def backTrack(first, check):
            
            if check == n:
                return True
            
            ans = False
            
            for i in range(first, n):
                if num[first] == "0" and i != first:
                    break
                for j in range(i + 1, n):
                    if num[i + 1] == "0" and i + 1 != j:
                        break
                    n1 = int(num[first:i+1])
                    n2 = int(num[i+1:j+1])
                    
                    for k in range(j + 1, n):
                        if num[j + 1] == '0' and j + 1 != k:
                            break
                        n3 = int(num[j+1:k+1])
                        if n1 + n2 == n3:
                            ans = ans or backTrack(i + 1, k + 1)
                        if ans == True:
                            return ans
            return ans
        
        return backTrack(0, 0)