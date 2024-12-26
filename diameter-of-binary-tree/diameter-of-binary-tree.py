# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(current):
            nonlocal ans
            if not current:
                return 0
            left = dfs(current.left)
            right = dfs(current.right)
            local_max = left + right
            ans = max(ans, local_max)
            return max(left, right) + 1
        dfs(root)
        return ans
