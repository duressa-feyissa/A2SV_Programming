class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        hold = []
        tmp = []
        for i in range(len(l)):
            hold = nums[l[i]:r[i]+1]
            hold.sort()
            x = 0
            for j in range(len(hold) - 1):
                if hold[j+1] - hold[j] != hold[1] - hold[0]:
                    x = 1
                    break
            if x == 0:
                tmp.append(True)
            else:
                tmp.append(False)
        return tmp
                
