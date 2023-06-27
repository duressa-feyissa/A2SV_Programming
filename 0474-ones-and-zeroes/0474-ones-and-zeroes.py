class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        memory = {}
        N = len(strs)
        ones = list(map(lambda x: x.count('1'), strs))
        zeros = list(map(lambda x: x.count('0'), strs))

        def dp(index, one, zero):
            if index >= N or one < 0 or zero < 0:
                return 0
            state = (index, one, zero)
            if state not in memory:
                count = dp(index+1, one-ones[index], zero-zeros[index])
                if one-ones[index] >= 0 and zero-zeros[index] >= 0:
                    count += 1
                count = max(count, dp(index+1, one, zero))
                memory[state] = count
            return memory[state]
        return dp(0,n,m)

                    
                