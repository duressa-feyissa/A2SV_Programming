class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        answer = 0
        occurance = defaultdict(int)
        for i in deliciousness:
            for k in range(22):
                answer += occurance[2**k - i]
            occurance[i] += 1                
        return answer % (10**9 + 7)
        