class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        bitHash = defaultdict(list)
        for item in arr:
            temp = bin(item).count('1')
            bitHash[temp].append(item)
        answer = []
        for key in sorted(bitHash.keys()):
            answer.extend(sorted(bitHash[key]))
        return answer
            
        
        