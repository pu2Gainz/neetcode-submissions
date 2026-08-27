class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 1):
                return 0
            area = 1
            grid[r][c] = 0
            for dr, dc in directions:
                if (0 <= r + dr < ROWS and 0 <= c + dc < COLS and grid[r + dr][c + dc] == 1):
                    area += dfs(r + dr, c + dc)
                
            return area

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    maxArea = max(maxArea, dfs(r, c))

        return maxArea