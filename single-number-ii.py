class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        array = [0] * 32
        sign = 0
        for num in nums:
            if num < 0:
                sign += 1
                num = num * -1
            i = 0
            while num:
                if num & 1:
                    array[i] += 1
                num = num >> 1
                i += 1
        answer = 0
        for i in range(32):
            if array[i] % 3:
                answer |= (1 << i)
        if sign % 3 != 0:
            answer = answer * -1
        return answer