class Solution: 
    def select(self, arr, i):
        small = arr[i]
        index = i
        for j in range(i,len(arr)):
            if small > arr[j]:
                small = arr[j]
                index = j
        return index
                    
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            j = Solution.select(self, arr, i)
            arr[i],arr[j] = arr[j], arr[i]
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
