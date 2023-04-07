class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        CanNotStartEdge = set()
        answer = set()
        for edge in edges:
            CanNotStartEdge.add(edge[1])
            answer.add(edge[0])
            if edge[0] in CanNotStartEdge:
                answer.remove(edge[0])
            if edge[1] in answer:
                answer.remove(edge[1])        
        return answer