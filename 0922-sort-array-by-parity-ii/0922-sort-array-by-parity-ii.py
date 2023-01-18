class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        nums.sort()
        numbers = defaultdict(list)
        for item in nums:
            if item % 2 == 0:
                numbers["even"].append(item)
            else:
                numbers["odd"].append(item)
        answer = []
        for i in range(len(nums)//2):
            answer.append(numbers["even"][i])
            answer.append(numbers["odd"][i])
        return answer
            
        
        