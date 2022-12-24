class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        new_dict = {}
        for index, item in enumerate(arr):
            new_dict[item] = index
        
        for index, item in enumerate(arr):
            if item * 2 in new_dict and index != new_dict[item * 2]:
                return True
            elif item / 2 in new_dict and index != new_dict[item / 2]:
                return True
        return False
        