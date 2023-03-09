# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        array1 = []
        array2 = []
        self.helper(root, p, array1)
        self.helper(root, q, array2)
        array2 = set(array2)
        for i in range(len(array1) - 1, -1, -1):
            if array1[i] in array2:
                return array1[i]

    def helper(self, root, node, stack):
        stack.append(root)
        if root.val == node.val:
            return
        elif root.val < node.val:
            self.helper(root.right, node, stack)
        else:
            self.helper(root.left, node, stack)