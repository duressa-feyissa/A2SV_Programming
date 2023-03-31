class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        HASH = {}
        for i in range(97, 123):
            HASH[chr(i)] = i - 97
        array = []
        for word in words:
            num = 0
            for c in word:
                num |= (1 << HASH[c])
            array.append(num)
        answer = 0
        length = list(map(lambda x: len(x), words))
        for i in range(n):
            for j in range(i + 1, n):
                if array[i] & array[j] == 0:
                    answer = max(answer, length[i] * length[j])
        return answer