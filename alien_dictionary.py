#Method: 1 using dfs
from collections import *
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        N = len(alien_dict)
        indegree = Counter()
        for i in range(1, N):
            length = min(len(alien_dict[i - 1]), len(alien_dict[i]))
            for j in range(length):
                if alien_dict[i][j] != alien_dict[i - 1][j]:
                    indegree[alien_dict[i][j]] += 1
                    graph[alien_dict[i - 1][j]].append(alien_dict[i][j])
                    break
    
        colors = [0] * 26
        answer = []
        def dfs(curr):
            index = ord(curr) - 97
            if colors[index] == 2:
                return False
            if colors[index] == 1:
                return True
            colors[index] = 1
            for node in graph[curr]:
                if dfs(node):
                    return True
            answer.append(curr)
            colors[index] = 2
            return False
        stat = False
        for key in list(graph.keys()):
            stat = stat or dfs(key)
        
        unique = set()
        for i in range(N):
            for j in range(len(alien_dict[i])):
                unique.add(alien_dict[i][j])
        visited = set(answer)
        
        for char in unique:
            if char not in visited:
                answer.append(char)
                visited.add(char)
        return answer[::-1]

#Method 2: using bfs
#User function Template for python3
from collections import *
class Solution:
    def findOrder(self,alien_dict, N, K):
        graph = defaultdict(list)
        N = len(alien_dict)
        indegree = Counter()
        for i in range(1, N):
            length = min(len(alien_dict[i - 1]), len(alien_dict[i]))
            for j in range(length):
                if alien_dict[i][j] != alien_dict[i - 1][j]:
                    indegree[alien_dict[i][j]] += 1
                    graph[alien_dict[i - 1][j]].append(alien_dict[i][j])
                    break
        
        unique = set()
        for i in range(N):
            for j in range(len(alien_dict[i])):
                unique.add(alien_dict[i][j])
        
        queue = deque([])
        visited = set()
        run = True
        answer = []
        
        for key in list(unique):
            if indegree[key] == 0:
                queue.append(key)
                visited.add(key)
          
        while queue and run:
            popped = queue.popleft()
            answer.append(popped)
            for node in graph[popped]:
                if node not in visited:
                    indegree[node] -= 1
                    if indegree[node] == 0:
                        queue.append(node)
                        visited.add(node)
                else:
                    run = False
        visited = set(answer)
        for char in unique:
            if char not in visited:
                answer.append(char)
                visited.add(char)
        return answer