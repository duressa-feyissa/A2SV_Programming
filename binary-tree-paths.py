# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        answer = []
        self.helper(root, [], answer)
        return answer
        
    def helper(self, root, stack, answer):
        
        if root and root.left is None and root.right is None:
            answer.append("->".join(stack + [str(root.val)]))
            return
        
        stack.append(str(root.val))
        
        if root and root.left is not None:
            self.helper(root.left, stack, answer)
        if root and root.right is not None:
            self.helper(root.right, stack, answer)
        if stack:
            stack.pop()