class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        count = 0
        counter = Counter(ages)
        for key1 in counter:
            for key2 in counter:
                if key2 > key1 * 0.5 + 7 and key1 >= key2:
                    if key1 != key2:
                        count += counter[key1] * counter[key2]
                    else:
                        count += counter[key1] * (counter[key2] - 1)
        return count
            


        