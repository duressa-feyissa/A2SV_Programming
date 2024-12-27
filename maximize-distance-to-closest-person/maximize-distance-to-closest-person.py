class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        n = len(seats)
        max_distance = 0

        if seats[0] == 0:
            i = 0
            while seats[i] == 0:
                i += 1
            max_distance = i  

        prev = -1
        for i in range(n):
            if seats[i] == 1:
                if prev == -1:
                    prev = i
                else:
                    distance = (i - prev) // 2
                    max_distance = max(max_distance, distance)
                    prev = i

        if seats[-1] == 0:
            i = n - 1
            while seats[i] == 0:
                i -= 1
            max_distance = max(max_distance, n - 1 - i)

        return max_distance
        