"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node', level=1) -> int:
        if not root:
            return 0
        if not root.children:
            return level
        Max = 0
        for node in root.children:
            Max = max(Max, self.maxDepth(node, level + 1))
        return Max