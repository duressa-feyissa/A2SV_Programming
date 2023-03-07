# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = self.helper(root)
        print(ans)
        return ans[1]
    
    def helper(self, root):
        if root == None:
            return [0, 0]
        
        res = [0, 0]
        left = self.helper(root.left)
        right = self.helper(root.right)
        
        res[1] = max(left[0] + right[0], max(left[1], right[1]))
        res[0] = max(left[0], right[0]) + 1
        return res
        
        
        
        
        