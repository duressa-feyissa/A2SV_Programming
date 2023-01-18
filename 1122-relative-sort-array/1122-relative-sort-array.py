class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        answer = []
        frequency = Counter(arr1)
        for item in arr2:
            temp = [item] * frequency[item]
            answer.extend(temp)
        nonExists = []
        for item in arr1:
            if item not in arr2:
                nonExists.append(item)
        answer.extend(sorted(nonExists))
        return answer
            