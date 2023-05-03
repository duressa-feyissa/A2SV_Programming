class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        parent = (i - 1) // 2
        while parent > -1 and arr[parent] < arr[i]:
            arr[parent], arr[i] = arr[i], arr[parent]
            i = parent
            parent = (i - 1) // 2
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        array = []
        for i in range(n):
            array.append(arr[i])
            self.heapify(array, n, i)
        return array
        
    
    def heapify_down(self, arr, current, last):
        left = 2 * current + 1
        right = 2 * current + 2
        small = current
        if left < last and arr[left] > arr[small]:
            small = left
        if right < last and arr[right] > arr[small]:
            small = right
        if small != current:
            arr[current], arr[small] = arr[small], arr[current]
            self.heapify_down(arr, small, last)        
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        array = self.buildHeap(arr, n)
        for i in range(n):
            last = n - i - 1
            array[last], array[0], = array[0], array[last]
            self.heapify_down(array, 0, last)
            arr[last] = array[last]
