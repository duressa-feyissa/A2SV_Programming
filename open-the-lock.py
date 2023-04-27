class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        check = set(deadends)
        visited = set()
        target = list(map(int, target))
        queue = deque([])
        count = -1
        adds = [-1, 1]
        if '0000' not in check:
            queue.append([0,0,0,0])
            visited.add('0000')
        
        while queue:
            N = len(queue)
            count += 1
            for _ in range(N):
                popped = queue.popleft()
                if target == popped:
                    return count
                for i in range(4):
                    flip = 0
                    for add in adds:
                        if add + popped[i] > 9:
                            flip = 0
                        elif add + popped[i] < 0:
                            flip = 9
                        else:
                            flip = add + popped[i]
                        change = popped[:]
                        change[i] = flip
                        val = "".join(list(map(str, change)))
                        if val not in visited and val not in check: 
                            queue.append(change[:])
                            visited.add(val)
        return -1