class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}

        for s, d, t in times:
            if s not in adj:
                adj[s] = []
            adj[s].append((t, d))

        minHeap = [(0, k)]
        visited = set()
        res = 0
        while minHeap:
            t, d = heapq.heappop(minHeap)
            if d in visited:
                continue
            res = t
            visited.add(d)
            if d not in adj:
                continue
            for nt, nd in adj[d]:
                if nd in visited:
                    continue
                heapq.heappush(minHeap, (t + nt, nd))

        return res if len(visited) == n else -1