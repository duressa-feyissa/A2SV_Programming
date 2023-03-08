# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    isbalance = True
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.isbalance
        
    def helper(self, root):
        if root == None:
            return 0
        left = self.helper(root.left) + 1
        right = self.helper(root.right) + 1
        
        if abs(left - right) > 1:
            self.isbalance = False
        
        return max(left, right)