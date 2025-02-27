# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        count = 0
        stack = [root]
        
        while stack:
            popped = stack.pop()
            if popped.left:
                stack.append(popped.left)
            if popped.right:
                stack.append(popped.right)
            count += 1
        
        return count
        