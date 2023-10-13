class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        answer = 0
        def dfs(root):
            nonlocal answer
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            curr = left + right - 1 + root.val
            answer += abs(curr)
            return curr
        dfs(root)
        return answer