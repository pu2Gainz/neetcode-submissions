class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        #build adj list
        if len(edges) != n - 1:
            return False

        adj = [[] for _ in range(n)]
        for first, second in edges:
            adj[first].append(second)
            adj[second].append(first)

        visited = set()
        def dfs(node, parent):
            if node in visited:
                return False
            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                if not dfs(child, node):
                    return False
            return True

            
            
        return dfs(0, -1) and len(visited) == n
        









