class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        rep = {i: i for i in range(row * col)}
        size = {i: 1 for i in range(row * col)}
        covers = {i: [-1,-1] for i in range(row * col)}

        dirs8 = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, -1], [1, -1], [-1,1]]

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        def find(node):
            if rep[node] == node:
               return rep[node]
            rep[node] = find(rep[node])
            return rep[node]

        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            if xrep != yrep:
                if size[xrep] > size[yrep]:
                    xrep, yrep = yrep, xrep
                size[yrep] += size[xrep]
                rep[xrep] = yrep
                covers[yrep][0] = min(covers[yrep][0], covers[xrep][0])
                covers[yrep][1] = max(covers[yrep][1], covers[xrep][1])
                if covers[yrep][0] == 0 and covers[yrep][1] == col - 1:
                    return True
            return False

        count = 0
        for x, y in cells:
            x, y = x - 1, y - 1
            pos1 = (x * col + y)
            covers[pos1] = [y,y]
            for dx, dy in dirs8:
                nr = x + dx
                nc = y + dy
                if inbound(nr, nc) and covers[nr * col + nc] != [-1, -1]:
                    pos2 = (nr * col + nc)
                    if union(pos1, pos2):
                        return count
            count += 1
        return count