# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root)[1]
        
    def helper(self, root):
        if root == None:
            return [0, True]
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        temp = abs(left[0] - right[0]) <= 1 and left[1] and right[1]
        
        return [(max(left[0], right[0]) + 1), temp]