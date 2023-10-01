# approache 1
class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        new_list = list(zip(ages, scores))
        new_list = sorted(new_list)
        @lru_cache(None)
        def helper(i):
            if i==0:
                return new_list[i][1]
            # max_value = new_list[i][1]
            max_value = 0
            for j in range(i):
                if new_list[i][1]>=new_list[j][1]:
                    max_value = max(max_value, helper(j))
            return max_value+new_list[i][1]
        return max(helper(i) for i in range(len(scores)))