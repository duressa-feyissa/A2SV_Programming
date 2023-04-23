# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    result = 0
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.helper(root, [])
        return self.result
        
    def helper(self, root, stack):
        if root == None:
            return
        stack.append(root.val)
        if len(stack) > 2 and stack[-3] % 2 == 0:
            self.result += stack[-1]
        
        self.helper(root.left, stack)
        self.helper(root.right, stack)        
        stack.pop()