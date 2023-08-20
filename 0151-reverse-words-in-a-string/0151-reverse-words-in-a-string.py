class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        words.reverse()
        array = []
        for word in words:
            temp = word.strip()
            if temp:
                array.append(temp)
        return " ".join(array)
        