class Solution:
    def racecar(self, target: int) -> int:
        queue = deque([(0, 1, 0)])
        visited = set()
        while queue:
            N = len(queue)
            for _ in range(N):
                position, speed, count = queue.popleft()
                if position == target:
                    return count
                else:
                    param1 = (position + speed, speed * 2, count + 1)
                    if (param1[0], param1[1]) not in visited:
                        if param1[0] <= target * 2 and param1[0] >= -target:
                            queue.append((position + speed, speed * 2, count + 1))
                            visited.add((param1[0], param1[1]))
                    inst = -1 if speed > 0 else 1
                    param2 = (position, inst, count + 1)
                    if (param2[0], param2[1]) not in visited:
                        if param2[0] <= target * 2 and param2[0] >= -target :
                            queue.append(param2)
                            visited.add((param2[0], param2[1]))
        
        
                
                
        