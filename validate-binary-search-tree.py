# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    decedant = 2 ** 32
    status = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.helper(root)
        return self.status
    
    def helper(self, root):
        if root == None:
            return 
        self.helper(root.right)
        if self.decedant <= root.val:
            self.status = False
        self.decedant = root.val
        left = self.helper(root.left)