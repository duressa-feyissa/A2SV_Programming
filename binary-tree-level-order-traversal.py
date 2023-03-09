# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        self.helper(root, 0, result)
        return list(result.values())

    def helper(self, root, level, result):
        if root == None:
            return
        result[level].append(root.val)
        self.helper(root.left, level + 1, result)
        self.helper(root.right, level + 1, result)