class Solution:
    def similarPairs(self, words: List[str]) -> int:
        data = list(map(set, words))
        data = list(map(lambda x: "".join(sorted(x)), data))
        data_dictionary = {}
        
        for item in data:
            if item in data_dictionary:
                data_dictionary[item] += 1
            else:
                data_dictionary[item] = 1
       
        total = 0
        for key in data_dictionary:
            value = data_dictionary[key]
            total += ((value) * (value - 1)) // 2
        
        return total