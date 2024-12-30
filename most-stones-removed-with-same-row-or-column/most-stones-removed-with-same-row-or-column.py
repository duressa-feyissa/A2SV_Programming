class Solution:
    def removeStones(self, stones):
        uf = self.UnionFind()

        for x, y in stones:
            uf.union((x, 0), (y, 1))

        return len(stones) - uf.component_count

    class UnionFind:
        def __init__(self):
            self.parent = {}
            self.component_count = 0

        def find(self, node):
            if node not in self.parent:
                self.parent[node] = node
                self.component_count += 1

            if self.parent[node] != node:
                self.parent[node] = self.find(self.parent[node])
            return self.parent[node]

        def union(self, node1, node2):
            root1 = self.find(node1)
            root2 = self.find(node2)

            if root1 != root2:
                self.parent[root1] = root2
                self.component_count -= 1
