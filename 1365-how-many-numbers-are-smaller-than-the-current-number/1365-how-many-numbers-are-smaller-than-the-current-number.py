class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        array = sorted(set(nums), reverse=True)
        frequency = Counter(nums)
        hash_map = defaultdict(int)
        length = len(nums)
        for key in array:
            length -= frequency[key]
            hash_map[key] = length
        answer=[]
        for item in nums:
            answer.append(hash_map[item])
        return answer
        
    
        
        