class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        counter = Counter()
        left = 0
        right = 0
        n = len(nums)
        answer = 1
        while right < n:
            if counter[nums[right]] < k:
                counter[nums[right]] += 1
                right += 1
            else:
                counter[nums[left]] -= 1
                left += 1
            answer = max(answer, right - left)
        return answer
        