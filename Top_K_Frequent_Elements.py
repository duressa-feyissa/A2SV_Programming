from statistics import mode
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        tmp = []
        for i in range(k):
            x = mode(nums)
            nums = list(filter(x.__ne__, nums))
            tmp.append(x)
        return tmp
