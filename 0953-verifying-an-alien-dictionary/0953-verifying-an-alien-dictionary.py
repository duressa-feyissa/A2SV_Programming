class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        new_dict = {}
        order = order[::-1]
        for i in range(len(order)):
            new_dict[order[i]] = i
        num = 0
        for i in range(len(words)):
            num = max(len(words[i]), num)
        
        i=0
        while i < num:
            j = 1
            k = 0
            while j < len(words):
                x, y = 27, 27
                if i < len(words[j-1]):
                    x = new_dict[words[j-1][i]]
                if i < len(words[j]):
                    y = new_dict[words[j][i]]
                if x < y:
                    return False
                elif x > y:
                    k+=1
                j+=1
            if k + 1 == j:
                return True
            i+=1
        return True
        
        