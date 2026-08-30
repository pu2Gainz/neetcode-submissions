class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        adj = collections.defaultdict(list)

        for (u, v), prob in zip(edges, succProb):
            adj[u].append((prob, v))
            adj[v].append((prob, u))

        visited = set()
        maxHeap = [(-1.0, start_node)]

        while maxHeap:
            p1, v1 = heapq.heappop(maxHeap)

            p1 = abs(p1)

            if v1 == end_node:
                return p1
            
            visited.add(v1)

            for p2, v2 in adj[v1]:
                if v2 not in visited:
                    heapq.heappush(maxHeap,(-p1 * p2, v2))

            
        return 0