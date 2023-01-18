class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        array = list(map(lambda a: a * a, nums))
        return sorted(array)
        