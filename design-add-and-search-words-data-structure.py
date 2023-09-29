class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.is_end = False

class  WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        current = self.root
        for c in word:
            index = ord(c) - ord('a')
            if not current.children[index]:
                current.children[index] = TrieNode()
            current = current.children[index]
        current.is_end = True

    def search(self, word: str) -> bool:
        def checker(word, pointer):
            for i, c in enumerate(word):
                if c == ".":
                    stat = False
                    for child in pointer.children:
                        if child:
                            stat = stat or checker(word[i+1:], child)
                    return stat
                index = ord(c) - ord('a')
                if not pointer.children[index]:
                    return False
                pointer = pointer.children[index]
            return pointer.is_end
        return checker(word, self.root)