from functools import lru_cache

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        # @lru_cache(None)
        def backtrack(i):
            if i == len(s):
                return [[]]
            
            result = []
            
            for j in range(i, len(s)):
                w = s[i: j+1]
                if w == w[::-1]:
                    partitions = backtrack(j+1)

                    for partition in partitions:
                        result.append([w] + partition)
            return result

        return backtrack(0)
