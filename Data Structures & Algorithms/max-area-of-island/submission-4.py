class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def bfs(r, c):
            count = 0
            q = deque([[r, c]])
            grid[r][c] = 0
            while(q):
                r, c = q.popleft()
                grid[r][c] = 0
                count += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                        q.append([nr, nc])
                        grid[nr][nc] = 0

            return count

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, bfs(r, c))

        return maxArea