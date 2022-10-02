class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if len(nums) == 1:
            return str(nums[0])
        new = list(map(str,nums))
        for i in range(len(new)):
            for j in range(i+1,len(new)):
                if new[j]+new[i] > new[i]+new[j]:
                    new[j],new[i] = new[i], new[j]
        tmp = "".join(new)
        if tmp == "0"*len(new):
            return "0"
        return tmp
        
