class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        seen = set()
        ans = -float('inf')

        for num in nums:
            if abs(num)>ans and -num in seen:
                ans = abs(num)
            seen.add(num)

        return -1 if ans==-float('inf') else ans

        