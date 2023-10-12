class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        add = 0
        N = len(s)
        s = s[::-1]
        power = power % modulo
        hashValue = hashValue % modulo
        for i in range(k):
            add = ((add * power) + ((ord(s[i]) - 96) % modulo)) % modulo
        answer= []
        power_k_minus_1 = pow(power, k-1, modulo)
        for i in range(k, N):
            if add == hashValue:
                answer.append(s[i-k: i])
            add = (add  - (((ord(s[i - k]) - 96) * power_k_minus_1) % modulo)) % modulo
            add = ((add % modulo) * power) % modulo
            add = ((add % modulo) + ((ord(s[i]) - 96) % modulo)) % modulo
        if add == hashValue:
            answer.append(s[N-k:])
        
        return answer[-1][::-1]