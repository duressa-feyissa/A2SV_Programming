class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        total = 0
        
        number_dict = {}
        
        for item in nums:
            if item in number_dict:
                number_dict[item] += 1
            else:
                number_dict[item] = 1
        
        for key in number_dict:
            times = number_dict[key]
            total += (times * (times - 1)) // 2
        
        return total