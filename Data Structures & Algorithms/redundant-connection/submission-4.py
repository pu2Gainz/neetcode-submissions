class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # n nodes from 1 to n
        # n edges now 
        n = len(edges)
        parent = [i for i in range(n + 1)]
        rank = [1] * (n + 1)

        def find(x):
            if not parent[x] == x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            pu = find(u)
            pv = find(v)

            if pu == pv:
                return False
            
            if rank[pu] < rank[pv]:
                pu, pv = pv, pu

            parent[pv] = pu
            if rank[pu] == rank[pv]:
                rank[pu] += 1
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

        return []

            