class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        edges = collections.defaultdict(list)

        for s, d, t in times:
            edges[s].append((t, d))

        minHeap = [(0, k)]
        visited  = set()
        total = 0
        while minHeap: 
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            total = time
            for t, d in edges[node]:
                if d not in visited:
            
                    heapq.heappush(minHeap, [time + t, d])

        return total if len(visited) == n else -1