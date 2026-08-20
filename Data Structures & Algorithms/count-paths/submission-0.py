class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        prevRow = [0] * n
        curRow = [0] * n
        for r in range(m - 1, -1, -1):
            curRow[n - 1] = 1
            for i in range(n - 2, -1, -1):
                curRow[i] = curRow[i + 1] + prevRow[i]
            prevRow = curRow[:]
        
        return curRow[0]
