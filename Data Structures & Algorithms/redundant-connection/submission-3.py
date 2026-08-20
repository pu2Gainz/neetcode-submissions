class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            ru, rv = find(u), find(v)
            if ru == rv:
                return False
            
            if rank[ru] < rank[rv]:
                ru, rv = rv, ru 
            
            parent[rv] = ru
            rank[ru] += rank[rv]

            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]
            

                
