class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        index = 0
        length = len(tickets)
        time = 0
        while True:
            if tickets[k] == 0:
                return time
            if tickets[index] > 0:
                tickets[index] -= 1
                time += 1
            index = (index + 1) % length
        return time
            
        