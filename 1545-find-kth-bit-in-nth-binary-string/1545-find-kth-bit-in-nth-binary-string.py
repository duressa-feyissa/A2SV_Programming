class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        return self.solve(n)[k - 1]
    
    def solve(self, n):
        if n == 1:
            return "0"
        temp = self.solve(n - 1)
        return self.solve(n- 1) + "1" + self.reverse(temp)

    def reverse(self, s):
        return self.invert(s)[::-1]
    
    def invert(self, s):
        inverted = ""
        for char in s:
            if char == "1":
                inverted += "0"
            else:
                inverted += "1"
        return inverted
    

        