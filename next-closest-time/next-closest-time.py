class Solution:
    def nextClosestTime(self, time: str) -> str:
        h, m = map(int, time.split(':'))
        digits = {h%10, m%10, h//10, m//10}
        
        while True:
            m += 1
            if m >= 60:
                h += 1
                m = m % 60
                if h >= 24:
                    h = h % 24
            if all([x in digits for x in [h%10, m%10, h//10, m//10]]):
                return f'{h:02}:{m:02}'