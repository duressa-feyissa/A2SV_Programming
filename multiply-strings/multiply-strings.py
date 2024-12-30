class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        M, N = len(num1), len(num2)
        if N > M:
            num1, num2 = num2, num1
            N, M = M, N
        
        mul = [[0] * (M*2) for _ in range(N)]

        for i in range(N-1,-1,-1):
            carry  = 0
            k = (M*2) - 1 - (N-1-i)
            for j in range(M-1,-1,-1):
                res = (int(num1[j]) * int(num2[i])) + carry
                carry = res // 10
                mul[N-i-1][k] = res % 10
                k -= 1
            mul[N-i-1][k] = carry
        
        carry = 0
        ans = ['0'] * (M*2)
        
        for i in range(len(ans)-1,-1,-1):
            res = carry
            for j in range(N):
                res += mul[j][i]
            ans[i] = str(res % 10)
            carry = res // 10

        ans = ''.join(ans).lstrip('0')
        if ans == '':
            return '0'
        return ans
            
                
                
                
        
            
        