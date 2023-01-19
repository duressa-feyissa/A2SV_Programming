class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remenderFrequency = [0]*k
        add = 0
        for x in nums:
            add += x%k
            remenderFrequency[add%k] += 1
        answer = remenderFrequency[0]
        for c in remenderFrequency:
            answer += (c * (c - 1))//2
        return answer

        