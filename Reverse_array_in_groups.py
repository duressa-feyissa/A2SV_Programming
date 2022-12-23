#User function template for Python

class Solution:	
    #Function to reverse every sub-array group of size k.
	def reverseInGroups(self, arr, N, K):
		i=0
		while i < N:
		    if i + K > N:
		        j=N-1
		    else:
		        j=i+K-1
		    k=j
		    while i <= j:
		        arr[i], arr[j] = arr[j], arr[i]
		        j-=1
		        i+=1
		    i=k+1
