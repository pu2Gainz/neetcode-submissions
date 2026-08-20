class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

        count = 0
        visited = set()
        def dfs(node, parent):
            if node in visited:
                return
            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                dfs(child, node)
            
        
        for node in range(n):
            if node not in visited:
                dfs(node, -1)
                count += 1
        
        return count