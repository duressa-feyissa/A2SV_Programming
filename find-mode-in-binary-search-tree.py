# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        most = defaultdict(int)
        def helper(root):
            nonlocal most
            if root == None:
                return
            helper(root.left)
            most[root.val] += 1
            helper(root.right)
        helper(root)
        most = sorted(most.items(), key=lambda x:x[1], reverse=True)
        return [m[0] for m in most if most[0][1] == m[1]]