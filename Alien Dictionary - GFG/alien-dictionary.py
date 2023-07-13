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


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends