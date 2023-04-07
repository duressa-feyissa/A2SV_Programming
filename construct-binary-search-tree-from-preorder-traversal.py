# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        n = len(preorder)
        def insert(root, index):
            if root == None:
                return TreeNode(preorder[index])
            if root.val > preorder[index]:
                root.left = insert(root.left, index)
            else:
                root.right = insert(root.right, index)
            return root
        
        root = None
        for i in range(n):
            root = insert(root, i)
        return root