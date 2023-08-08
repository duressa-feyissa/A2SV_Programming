class ThroneInheritance:

    def __init__(self, kingName: str):
        self.king = kingName
        self.graph = defaultdict(list)
        self.dead = set()
        self.parent = {}
        
    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        self.parent[childName] = parentName

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        answer = []
        visited = set()
        def dfs(curr):
            numberChildrenInOrder = 0
            visited.add(curr)
            for node in self.graph[curr]:
                if node in visited:
                    numberChildrenInOrder += 1 
            if len(self.graph[curr]) == 0 or (numberChildrenInOrder == len(self.graph[curr])):
                if curr == self.king:
                    return
                return dfs(self.parent[curr])
            for child in self.graph[curr]:
                if child not in visited:
                    if child not in self.dead:
                        answer.append(child)                    
                    return dfs(child)
        dfs(self.king)
        if self.king not in self.dead:
            return [self.king] + answer 
        return answer
                
            


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()