class Solution:

    def __init__(self):
        self.result = []
        self.back = []
        self.check = set()
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.helper(root, target.val, k, [])
        self.check.add(target.val)
        n = len(self.back)
        print(self.back)
        for i in range(n - 1, -1, -1):
            self.search(self.back[i], k - (n - i))
        return self.result

    def helper(self, root, target, k, stack):
        if root == None:
            return
        stack.append(root)
        self.helper(root.left, target, k, stack)
        self.helper(root.right, target, k, stack)
        if len(stack) > k and stack[-(k + 1)].val == target:
            self.result.append(root.val)
        stack.pop()
        if root.val == target:
            self.back = stack.copy()

    def search(self, root, k):
        if root == None:
            return
        if root.val in self.check:
            return
        if k == 0:
            self.check.add(root.val)
            self.result.append(root.val)
            return
        self.search(root.left, k - 1)
        self.search(root.right, k - 1)
        self.check.add(root.val)
        
        