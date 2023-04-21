class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        adjacent = defaultdict(list)
        for dislike in dislikes:
            adjacent[dislike[0]].append(dislike[1])
            adjacent[dislike[1]].append(dislike[0])
            
        colors = {}
        def dfs(current, color):
            
            colors[current] = color
            
            for edge in adjacent[current]:
                if edge not in colors:
                    if not dfs(edge, 1 ^ color):
                        return False
                elif colors[edge] == color:
                    return False
            return True
        
        for key in list(adjacent.keys()):
            if key not in colors:
                if not dfs(key, 0):
                    return False
        return True