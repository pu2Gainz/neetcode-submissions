class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]

        def dfs(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == "1"):
                return False
            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)
            return True
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    count += 1
        return count
                    