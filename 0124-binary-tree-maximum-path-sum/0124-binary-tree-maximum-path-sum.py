# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        Max = float('-inf')
        def dfs(root):
            nonlocal Max
            if not root:
                return 0
            greater, both = 0, 0
            left = dfs(root.left)
            if left > 0:
                greater, both = max(left, greater), left
            right = dfs(root.right)
            if right > 0:
                both += right
                greater = max(greater, right)
            if greater >= both:
                Max = max(Max, root.val + greater)
            else:
                Max = max(Max, root.val + both)
            Max = max(Max, root.val)
            return root.val + greater
        dfs(root)
        return Max
            
    
        