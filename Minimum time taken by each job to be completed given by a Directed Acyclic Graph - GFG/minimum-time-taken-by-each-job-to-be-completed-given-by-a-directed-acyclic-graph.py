from typing import List
from collections import *
from typing import List


class Solution:
    def minimumTime(self, n : int,m : int, edges : List[List[int]]):
        graph = defaultdict(list)
        indegree = Counter()
        for x, y in edges:
            graph[x].append(y)
            indegree[y] += 1
        
        queue = deque([])
        for i in range(1, n+1):
            if indegree[i] == 0:
                queue.append(i)
        answer = [1] * n
        time = 1
        while queue:
            N = len(queue)
            for _ in range(N):
                current = queue.popleft()
                answer[current - 1] = time
                for node in graph[current]:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        queue.append(node)
            time += 1
    
        return answer
        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends