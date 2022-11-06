class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        total = sum(chalk)
        j = 1
        if k > total:
            k = k % total
        while True:
            if total <= k:
                k -= total
            else:
                for i in range(len(chalk)):
                    if chalk[i] <= k:
                        k -= chalk[i]
                    else:
                        return i
