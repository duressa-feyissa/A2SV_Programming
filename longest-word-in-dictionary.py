class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index] 
        current.is_end = True

    def checker(self, word):
        current = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')        
            current = current.children[index]
            if not current.is_end:
                return False 
        return True

    def longestWord(self, words: List[str]) -> str:
        possibles = []
        for word in words:
            self.insert(word)
        Max = 0
        for word in words:
            if self.checker(word):
                n = len(word)
                Max = max(Max, n)
                possibles.append([word, n])
        N = len(possibles)
        if N == 0:
            return ""
        filtered_possibles = []
        for i in range(N):
            if possibles[i][1] == Max:
                filtered_possibles.append(possibles[i][0])
        filtered_possibles.sort()
        return filtered_possibles[0]