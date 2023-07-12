class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:

        def add_parent(cur, parent):
            if cur:
                cur.parent = parent
                add_parent(cur.left, cur)
                add_parent(cur.right, cur) 
                
        add_parent(root, None)  
        queue = deque([target])
        visited = set()
        answer = []
        while queue and k >= 0:
            N = len(queue)
            for _ in range(N):
                popped = queue.popleft()
                if not popped or popped in visited:
                    continue
                visited.add(popped)
                if k == 0:
                    answer.append(popped.val)
                queue.append(popped.left)
                queue.append(popped.right)
                queue.append(popped.parent)
            k -= 1
        
        return answer