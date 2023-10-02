class TrieNode:
    
    def __init__(self):
        self.children = [None] * 26
        self.index = 0
        
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        self.N = 0
        
    def insert(self, word):
        current = self.root
        for i, c in enumerate(word):
            index = ord(c) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current.index = i
            current = current.children[index]
        
    def helper(self, word, wordDict, pointer):
        result = []
        n = len(word)
        for i, w in enumerate(word):
            index = ord(w) - ord('a')
            if not pointer.children[index] or  pointer.index > self.N:
                return [[None, False]]
            if pointer.index == self.N - 1 and i == n -1:
                return [[word, True]]
            pointer = pointer.children[index]
        if pointer.index > self.N:
            return [[None, False]]
        for wrd in wordDict:
            sResult = self.helper(wrd, wordDict, pointer)
            for val in sResult:
                if val[1]:
                    result.append([word + " " + val[0], val[1]])
        return result

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        trie = Trie()
        trie.insert(s)
        trie.N = len(s)
        result = []
        current = trie.root
        for word in wordDict:
            result.extend(trie.helper(word, wordDict, current))
        ans = []
        for pos in result:
            if pos[1]:
                ans.append(pos[0])        
        return ans
        