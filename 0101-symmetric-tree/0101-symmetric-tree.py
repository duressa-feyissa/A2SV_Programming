# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        array1, array2 = [], []
        self.helper1(root, array1)
        self.helper2(root, array2)
        if array1 == array2:
            return True
        return False
        
        
    def helper1(self, root, array):
        if root == None:
            array.append(None)
            return
        array.append(root.val)
        self.helper1(root.left, array)
        self.helper1(root.right, array)
    
    def helper2(self, root, array):
        if root == None:
            array.append(None)
            return
        array.append(root.val)
        self.helper2(root.right, array)
        self.helper2(root.left, array)
        
        
        
        
        
        
        