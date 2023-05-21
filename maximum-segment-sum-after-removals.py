class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N = len(nums)
        rep = {i: i for i in range(N)}
        size = {i: 1 for i in range(N)}
        totalAdds = {i: nums[i] for i in range(N)}
        array = [0] * N
        Max = removeQueries[-1]

        def inbound(index):
            return 0 <= index < N

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
                totalAdds[yrep] += totalAdds[xrep]
                return True
            return False
        
        answer = [0]
        for i in range(N - 1, 0, -1):
            index = removeQueries[i]
            before = index - 1
            after = index + 1
            if inbound(before) and array[before]:
                union(before, index)
            if inbound(after) and array[after]:
                union(after, index)
            parent = find(index)
            if totalAdds[parent] > totalAdds[Max]:
                Max = parent
            answer.append(totalAdds[find(Max)])
            array[index] = nums[index]

        return answer[::-1]