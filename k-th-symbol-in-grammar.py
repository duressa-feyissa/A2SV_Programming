class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 or (n == 2 and k == 1):
            return 0
        if n == 2 and k == 2:
            return 1
        
        isInverted = False
        if k > 2 ** (n - 1) // 2:
            isInverted = True
            k = k - (2 ** (n - 1) // 2)
        previous_th_k = self.kthGrammar(n - 1, k)
        
        if isInverted == True:
            if previous_th_k == 1:
                return 0
            return 1
        return previous_th_k
        
    """
    def solve(self, n):
        
        if n == 1:
            return ['0']
        if n == 2:
            return ['0', '1']
                
        previous = self.solve(n - 1)
        previousflipped = list(map(self.flip, previous))
        previous.extend(previousflipped)
        return previous
    
    def flip(self, c):
        if c == '0':
            return '1'
        else:
            return '0'
    
    """