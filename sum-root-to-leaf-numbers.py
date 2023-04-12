# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    answer = 0
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.answer = 0
        self.helper(root, 0)
        return self.answer
        
        
    def helper(self, root, add):
        
        if root.left == None and root.right == None:
            self.answer += (add * 10) + root.val
            return
        
        if root.left:
            self.helper(root.left, (add * 10) + root.val)
        if root.right:
            self.helper(root.right, (add * 10) + root.val)