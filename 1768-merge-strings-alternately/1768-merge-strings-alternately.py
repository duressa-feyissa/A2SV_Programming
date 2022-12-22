class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merge = ""
        if len(word1) > len(word2):
            for i in range(len(word2)):
                merge += word1[i]
                merge += word2[i]
                if i == len(word2) - 1:
                    merge += word1[i+1:]
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                merge += word1[i]
                merge += word2[i]
                if i == len(word1) - 1:
                    merge += word2[i+1:]
        else:
            for i in range(len(word1)):
                merge += word1[i]
                merge += word2[i]
        return merge
        