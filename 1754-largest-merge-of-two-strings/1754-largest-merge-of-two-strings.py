class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        merge = []
        ptr1 = 0
        ptr2 = 0
        while ptr1 < m and ptr2 < n:
            if word1[ptr1:] > word2[ptr2:]:
                merge.append(word1[ptr1])
                ptr1 += 1
            else:
                merge.append(word2[ptr2])
                ptr2 += 1
        return "".join(merge) + word1[ptr1:] + word2[ptr2:]
        