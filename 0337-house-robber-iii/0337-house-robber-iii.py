# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memory = {}
        def dp(current):
            if not current:
                return 0
            if current in memory:
                return memory[current]
            val1 = current.val
            if current.left:
                val1 += dp(current.left.left) + dp(current.left.right)
            if current.right:
                val1 += dp(current.right.left) + dp(current.right.right)
            val2 = dp(current.left) + dp(current.right)
            memory[current] = max(val1, val2)       
            return memory[current]
        return dp(root)
            

            