class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        check = set(nums)
        count = len(check)
        for item in nums:
            temp = str(item)[::-1]
            temp = int(temp)
            if temp not in check:
                count += 1
                check.add(temp)
        return count