# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        count = 0
        def helper(root):
            nonlocal count
            if root == None:
                return [0, 0]
            left = helper(root.left)
            right = helper(root.right)
            nodes = left[1] + right[1] + 1
            total = left[0] + right[0] + root.val 
            average = total // nodes
            if average == root.val:
                count += 1
            return [total, nodes]
        helper(root)
        return count