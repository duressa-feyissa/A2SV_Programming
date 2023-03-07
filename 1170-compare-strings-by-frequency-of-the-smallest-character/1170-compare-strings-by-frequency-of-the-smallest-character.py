class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        WordFrequency = []
        QueryFrequency = []

        for word in words:
            chars = Counter(word)
            chars = sorted(chars.items())
            WordFrequency.append(chars[0][1])

        result = []    
        WordFrequency.sort()
        n = len(words)

        for query in queries:
            chars = Counter(query)
            chars = sorted(chars.items())
            QueryFrequency.append(chars[0][1])
        
        for freq in QueryFrequency:
            left = 0
            right = n - 1

            while left <= right:
                middle = (left + right) // 2
                if WordFrequency[middle] <= freq:
                    left = middle + 1
                else:
                    right = middle - 1
            result.append(n - left)
        
        return result








        