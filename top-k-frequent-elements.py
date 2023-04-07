class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = list(Counter(nums).items())
        n = len(counter)
        index = [0]
        def QuickSort(left, right, index):
            if left > right:
                return
            pivot = counter[right][1]
            i = left
            for j in range(left,right):
                if counter[j][1] <= pivot:
                    counter[i], counter[j] = counter[j], counter[i]
                    i += 1
            
            counter[i], counter[right] = counter[right], counter[i]
            if n - i - 1 == k:
                index[0] = i + 1
                return 
            elif n - i - 1 > k:
                QuickSort(i + 1, right, index)
            else:
                QuickSort(left, i - 1, index)
        QuickSort(0, n - 1, index)
        return [counter[i][0] for i in range(index[0], n)]