# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        count = 0
        prefix = defaultdict(int)
        prefix[0] = 1
        
        def helper(root, add):
            nonlocal count
            if root == None:
                return
            
            add += root.val
            count += prefix[add - targetSum]
            prefix[add] += 1          
            helper(root.left, add)
            helper(root.right, add)
            prefix[add] -= 1
            if prefix[add] == 0:
                del prefix[add]
            add -= root.val
        
        helper(root, 0)
        
        return count