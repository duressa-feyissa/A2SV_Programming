class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new = list(map(int,nums))
        new.sort(reverse=True)
        return str(new[k-1])
