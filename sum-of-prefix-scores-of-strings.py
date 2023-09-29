class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.prefix = 0
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
            current.prefix += 1
    
    def count(self, word):
        current = self.root
        count = 0
        for c in word:
            index = ord(c) - ord('a')
            current = current.children[index]
            count += current.prefix
        return count

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        answer = []
        for word in words:
            answer.append(trie.count(word))
        return answer