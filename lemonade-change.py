class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = Counter()
        for bill in bills:
            if bill == 5:
                counter[bill] += 1
            elif bill == 10:
                if counter[5] < 1:
                    return False
                counter[5] -= 1
                counter[10] += 1
            else:
                if counter[10] > 0 and counter[5] > 0:
                    counter[5] -= 1
                    counter[10] -= 1
                elif counter[5] > 2:
                    counter[5] -= 3
                else:
                    return False
        return True