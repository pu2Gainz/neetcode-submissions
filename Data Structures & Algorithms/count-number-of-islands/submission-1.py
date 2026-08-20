class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == "1":
                grid[r][c] = "0"
                for dr, dc in directions:
                    dfs(r + dr, c + dc)
            else:
                return
            
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    islands += 1
                    dfs(i, j)
        return islands
