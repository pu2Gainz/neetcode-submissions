class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and (r, c) not in visited and grid[r][c] == "1"):
                return 
            visited.add((r, c))

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc)

        count = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and (i, j) not in visited:
                    count += 1
                    dfs(i, j)
        return count
                    