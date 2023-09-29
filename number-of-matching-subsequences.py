class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True
    
    def checker(self, s, word):
        current = self.root
        i, j, n, m  = 0, 0, len(s), len(word)
        while i < m and j < n:
            index = ord(word[i]) - ord('a')
            if current.children[index]:
                current = current.children[index]
                i += 1
                j += 1
            else:
                index = ord(s[j]) - ord('a')
                current = current.children[index]
                j += 1
        return i == m

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        trie = Trie()
        trie.insert(s)
        counter = {}
        count = 0
        for word in words:
            if word not in counter:
                counter[word] = trie.checker(s, word)
                if counter[word]:
                    count += 1
            else:
                if counter[word]:
                    count += 1
        return count