# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        array = []
        self.helper(root, array)
        return array
    
    def helper(self, root, array):
        if root == None:
            return
        array.append(root.val)
        self.helper(root.left, array)
        self.helper(root.right, array)
        
    

        
            