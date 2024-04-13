class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        q = deque(range(len(deck)))
        res = [0]*len(deck)

        for c in deck:
            i = q.popleft()
            res[i]=c

            if q:
                q.append(q.popleft())
        return res