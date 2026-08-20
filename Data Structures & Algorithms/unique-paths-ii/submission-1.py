class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        M = len(obstacleGrid)
        N = len(obstacleGrid[0])
        if obstacleGrid[M - 1][N - 1] or obstacleGrid[0][0]:
            return 0

        prevRow = [0] * N
        curRow = [0] * N
        for r in range(M - 1, -1, -1):
            if r == M - 1:
                curRow[N - 1] = 1
            else:
                curRow[N - 1] = 0 if obstacleGrid[r][N - 1] else prevRow[N - 1]
            for c in range(N - 2, -1, -1):
                if obstacleGrid[r][c]:
                    curRow[c] = 0
                else:
                    curRow[c] = curRow[c + 1] + prevRow[c]
            prevRow = curRow.copy()

        return curRow[0]