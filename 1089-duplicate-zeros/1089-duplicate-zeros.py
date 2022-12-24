class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        number_dict = {}
        
        for index, item in enumerate(arr):
            number_dict[index] = item
        total = 0
        LENGTH = len(arr)
        
        item = 0
        while item < LENGTH:
            if number_dict[item - total] == 0:
                arr[item]=0
                total+=1
                item+=1
                if item < LENGTH:
                    arr[item] = 0
            else:
                arr[item] = number_dict[item - total]
            item+=1