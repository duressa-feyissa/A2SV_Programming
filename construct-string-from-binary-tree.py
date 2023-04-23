# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def helper(root):
            if root.left == None and root.right == None:
                return str(root.val)
            left = ""
            right = ""
            if root.left:
                left = "({})".format(helper(root.left))
            else:
                if root.right:
                    left = '()'
            if root.right:
                right = "({})".format(helper(root.right))
            return str(root.val) + left + right
        return helper(root)