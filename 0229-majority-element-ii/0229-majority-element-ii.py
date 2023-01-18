class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        frequency = Counter(nums)
        answer = []
        check = len(nums) // 3
        for key, value in frequency.items():
            if value > check:
                answer.append(key)
        return answer
        