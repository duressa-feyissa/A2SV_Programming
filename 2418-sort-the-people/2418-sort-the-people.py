class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        hash_map = {}
        for index in range(len(names)):
            hash_map[heights[index]] = names[index]
        answer = sorted(hash_map, reverse=True)
        return [hash_map[key] for key in answer]
        
        """
        for i in range(len(names) - 1, -1, -1):
            for j in range(1,i+1):
                if heights[j - 1] < heights[j]:
                    heights[j-1], heights[j] = heights[j], heights[j-1]
                    names[j - 1], names[j] = names[j], names[j-1]
        """
                    
        