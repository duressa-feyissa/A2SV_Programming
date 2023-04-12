class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        array = [True] * (right + 1)
        array[0], array[1] = False, False
        for i in range(2, ceil(sqrt(right)) + 1):
            if array[i]:
                for j in range(i * i, right + 1, i):
                    array[j] = False

        Min = float('inf')
        check = [-1,-1]
        answer = [-1, -1]
        count = 0
        for i in range(left, right + 1):
            if array[i]:
                if count == 0:
                    check[0] = i
                else:
                    check[1] = i
                count += 1
            if count == 2:
                if (check[1] - check[0]) < Min:
                    Min = check[1] - check[0]
                    answer = check[:]
                check[0] = check[1] 
                count -= 1

        if answer[0] != -1 and answer[1] != -1:
            return answer
        return [-1, -1]
