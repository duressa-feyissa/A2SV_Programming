class LockingTree:
    def __init__(self, parent: List[int]):
        self.parent = parent
        length = len(parent)
        self.status = [-2] * (length + 1)
        self.graph = defaultdict(list)
        for i in range(1, length):
            self.graph[parent[i]].append(i)
    def lock(self, num: int, user: int) -> bool:
        if self.status[num] == -2:
            self.status[num] = user
            return True
        return False
        
    def unlock(self, num: int, user: int) -> bool:
        if self.status[num] == user:
            self.status[num] = -2
            return True
        return False
            
    def upgrade(self, num: int, user: int) -> bool:
        if self.status[num] != -2:
            return False
        haveLockedDescendant = 0
        
        if self.dfs(num, set(), 0) == 0:
            return False
        
        haveLockedAncestors = False
        node = num
        while node != -1:
            if self.status[self.parent[node]] != -2:
                haveLockedAncestors = True
            node = self.parent[node]
        
        if haveLockedAncestors:
            return False
        self.dfs(num, set(), 1)            
        self.status[num] = user
        return True
    
    def dfs(self, curr, visited, action):
        visited.add(curr)
        count = 0
        if action:
            self.status[curr] = -2
        if not action and self.status[curr] != -2:
            count = 1
        for node in self.graph[curr]:
            if node not in visited:
                count += self.dfs(node, visited, action)
        return count
            
        
        
        
        
        
        
        
        
        
        
        
        