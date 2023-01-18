class Solution:
    def findLHS(self, nums: List[int]) -> int:
        array = sorted(set(nums))
        indexHash = defaultdict(list)
        for index, value in enumerate(sorted(nums)):
            indexHash[value].append(index)
        largest = 0
        for index in range(1, len(array)):
            if array[index] - array[index-1] == 1:
                largest = max(indexHash[array[index]][-1]
                              - indexHash[array[index-1]][0] + 1, largest)
        return largest
        
                
            
            
        