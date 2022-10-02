class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        new = nums.copy()
        new.sort()
        while True:
            x = 0
            for i in range(1,len(new) - 1):
                if (new[i-1] + new[i+1]) / 2 == new[i]:
                    new[i],new[i-1] = new[i-1],new[i]
                else:
                    x += 1
            if x == len(new) - 2:
                return new
