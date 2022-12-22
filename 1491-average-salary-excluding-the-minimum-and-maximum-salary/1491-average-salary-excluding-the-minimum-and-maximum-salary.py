class Solution:
    def average(self, salary: List[int]) -> float:
        MIN = min(salary)
        MAX = max(salary)
        add = 0
        for i in salary:
            if i == MIN or i == MAX:
                pass
            else:
                add+=i
        return add/(len(salary) - 2)
        