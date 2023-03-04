class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hold = nums.copy()
        nums.sort()
        i=0
        j=len(nums)-1
        tmp=[]
        while i <= j:
            if nums[i] + nums[j] == target:
                tmp.append(nums[i])
                tmp.append(nums[j])
                break
            elif nums[i] + nums[j] > target:
                j-=1
            else:
                i+=1
        new =[]
        for i in range(len(hold)):
            if hold[i] in tmp:
                new.append(i)
                tmp.remove(hold[i])
                if len(tmp) == 0:
                    break
        return new