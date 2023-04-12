"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node', level=1, visited=set()) -> int:
        if not root:
            return 0
        if not root.children:
            return level
        visited.add(root)
        Max = 0
        for node in root.children:
            if node not in visited:
                Max = max(Max, self.maxDepth(node, level + 1, visited))
        return Max