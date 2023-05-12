class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        counter = Counter()
        for x, y in adjacentPairs:
            graph[x].append(y)
            graph[y].append(x)
            counter[x] += 1
            counter[y] += 1
        once = None
        visited = set()
        for key, val in counter.items():
            if val == 1:
                once = key
                visited.add(key)
                break
        stack = [once]
        answer = []
        while stack:
            current = stack.pop()
            answer.append(current)
            for node in graph[current]:
                if node not in visited:
                    stack.append(node)
                    visited.add(node)
        return answer