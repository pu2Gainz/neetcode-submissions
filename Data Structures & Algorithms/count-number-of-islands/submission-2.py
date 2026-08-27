class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def bfs(r, c):
            q = deque([[r, c]])
            while q:
                qLen = len(q)
                for i in range(qLen):
                    row, col = q.popleft()
                    for dr, dc in directions:
                        nr = row + dr
                        nc = col + dc
                        if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == "1":
                            q.append([nr, nc])
                            grid[nr][nc] = "0"
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    count += 1
                    bfs(i, j)

        return count
                    