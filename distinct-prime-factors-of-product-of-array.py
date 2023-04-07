class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        answer = set()
        
        def prime(num):
            dividor = 2
            while num > 1:
                if num % dividor == 0:
                    answer.add(dividor)
                    num /= dividor
                else:
                    dividor += 1
        
        for num in nums:
            prime(num)
        
        return len(answer)