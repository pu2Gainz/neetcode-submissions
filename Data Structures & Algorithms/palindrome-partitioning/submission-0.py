class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        cur = []

        def backtrack(i, cur):
            if i == len(s):
                res.append(cur.copy())
                return 
            
            for j in range(i, len(s)):
                w = s[i: j+1]
                if w == w[::-1]:
                    cur.append(w)
                    backtrack(j+1, cur)
                    cur.pop()

            return

        backtrack(0, cur)
        return res