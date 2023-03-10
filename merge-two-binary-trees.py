# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(root1, root2):
            if root1 == None and root2 == None:
                return None
            if root1 == None:
                root1 = TreeNode()    
            if root2 == None:
                root2 = TreeNode()
            return TreeNode(root1.val + root2.val, helper(root1.left, root2.left), helper(root1.right, root2.right))
        return helper(root1, root2)