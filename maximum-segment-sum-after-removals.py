class Solution:
    def maximumSegmentSum(self, nums: List[int], removeQueries: List[int]) -> List[int]:
        N = len(nums)
        rep = {i: i for i in range(N)}
        size = {i: 1 for i in range(N)}
        sums = {i: nums[i] for i in range(N)}
        array = [0] * N
        Max = removeQueries[-1]

        def inbound(index):
            return 0 <= index < N

        def modify(newIndex, index):
            if inbound(newIndex) and array[newIndex]:
                newIndexParent = find(newIndex)
                indexParent = find(index)
                if union(newIndex, index):
                    parent = find(index)
                    if parent == newIndexParent:
                        sums[parent] += sums[indexParent]
                    else:
                         sums[parent] += sums[newIndexParent]
        
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
                return True
            return False
        answer = [0]
        for i in range(N - 1, 0, -1):
            index = removeQueries[i]
            modify(index - 1, index)
            modify(index + 1, index)        
            parent = find(index)
            if sums[parent] > sums[Max]:
                Max = parent
            answer.append(sums[find(Max)])
            array[index] = nums[index]

        return answer[::-1]