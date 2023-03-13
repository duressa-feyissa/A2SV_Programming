# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = defaultdict(list)
        
        def helper(root, row, col):
            nonlocal result
            if root == None:
                return
            helper(root.left, row + 1, col - 1)
            helper(root.right, row + 1, col + 1)
            result[col].append((row, root.val))
        
        helper(root, 0, 0)
        
        answer = []
        
        for _key in sorted(result.keys()):
            
            temp = defaultdict(list)
            for k, v in result[_key]:
                temp[k].append(v)
            
            res = []
            for key in sorted(temp.keys()):
                res.extend(sorted(temp[key]))   
            answer.append(res)
        
        return answer
            
            
        
            
            