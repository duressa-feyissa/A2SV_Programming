class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for key in sorted(count):
            while count[key] > 0:
                for i in range(groupSize):
                    if count[key + i] <= 0:
                        return False
                    count[key + i] -= 1
                    
        return True
