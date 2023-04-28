class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        N = len(labels)
        answer = [0] * N
        adjacent = defaultdict(list)

        for edge in edges:
            adjacent[edge[0]].append(edge[1])
            adjacent[edge[1]].append(edge[0])

        def dfs(current, visited):
            visited.add(current)
            counter = Counter(labels[current])
            if len(adjacent[current]) == 1:
                answer[current] += 1
            for key in adjacent[current]:
                if key not in visited:
                    T = dfs(key, visited)
                    for k in T.keys():
                        counter[k] += T[k]
            answer[current] = counter[labels[current]]
            return counter
        dfs(0, set())
        return answer