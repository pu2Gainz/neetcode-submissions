class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        res = n
        dsu = DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, x):
        if not self.parent[x] == x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)

        if pu == pv: 
            return False

        ru, rv = self.rank[pu], self.rank[pv]

        if ru < rv:
            pu, pv = pv, pu
        
        if self.rank[pu] == self.rank[pv]:
            self.rank[pu] += 1
        self.parent[pv] = pu

        return True
