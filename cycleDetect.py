from typing import List
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
	    
	    colors = defaultdict(int)
	    
	    def dfs(current, parent):
	        if colors[current] == 2:
	            return False
	        if colors[current] == 1:
	            return True
	        colors[current] = 1
	        for node in adj[current]:
	            if parent != node and dfs(node, current):
	                return True
	        colors[current] = 2
	        return False
	        
	    for v in range(V):
	        if colors[v] == 0 and adj[v]:
	            if dfs(v, -1):
	               return True
	    return False
	        
	


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends