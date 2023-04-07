class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        answer = set()
        prime = [2,3,5,7,11,13,17,19,23,29,31]
        
        def factor(num):
            i = 0
            while i < 11 and num > 1:
                if num % prime[i] == 0:
                    answer.add(prime[i])
                    num /= prime[i]
                else:
                    i += 1
            if num != 1:
                answer.add(num)
        
        for num in nums:
            factor(num)
        
        return len(answer)