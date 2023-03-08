# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        subarray = []
        array = []
        self.PreOrderTraversal(subRoot, subarray)
        self.PreOrderTraversal(root, array)
        return  "".join(subarray) in "".join(array)
        
    def PreOrderTraversal(self, root, array):
        if root == None:
            array.append("#" + str(None))
            return
        array.append(str("*" + str(root.val)))
        self.PreOrderTraversal(root.left, array)
        self.PreOrderTraversal(root.right, array) 
        
        

        