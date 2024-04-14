# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if root != None:
            if (root.left != None):
                if (root.left.left == None and root.left.right == None):
                    return root.left.val + self.sumOfLeftLeaves(root.right)
                else:
                    return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
            elif root.right != None:
                return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
            else:    
                return 0

        else:
            return 0