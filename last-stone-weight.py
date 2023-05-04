class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        self.buildHeap(stones, len(stones))
        
        while len(stones) > 1:
            values = [-1, -1]
            for i in range(2):
                values[i] = stones[0]
                stones[0] = stones[-1]
                stones.pop()
                self.heapify_down(stones, 0, len(stones))
            if values[0] != values[1]:
                stones.append(values[0] - values[1])
                self.heapify_up(stones, len(stones) - 1)
        if stones:
            return stones[0]
        return 0
        
    def heapify_down(self, arr, current, last):
        left = 2 * current + 1
        right = 2 * current + 2
        large = current
        if left < last and arr[left] > arr[large]:
            large = left
        if right < last and arr[right] > arr[large]:
            large = right
        if large != current:
            arr[current], arr[large] = arr[large], arr[current]
            self.heapify_down(arr, large, last) 
    
    def heapify_up(self, arr, i):
        parent = (i - 1) // 2
        while parent > -1 and arr[parent] < arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
            parent = (i - 1) // 2
        
    def buildHeap(self, array, n):
        for i in range(n // 2 - 1, -1, -1):
            self.heapify_down(array, i, n)