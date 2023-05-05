class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter()
        for word in words:
            counter[word] += 1
        array = []
        for word in counter:
            array.append((-counter[word], word))
        heapify(array)
        answer = []
        for _ in range(k):
            _, word = heappop(array)
            answer.append(word)
        return answer