class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific = []
        atlantic = []
        for i in range(rows):
            pacific.append([i, 0])
            atlantic.append([i, cols - 1])

        for j in range(cols):
            pacific.append([0, j])
            atlantic.append([rows - 1, j])

        pac = set()
        atl = set()

        direction = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        def bfs(r, c, ocean):
            if (r, c) in ocean:
                return
            q = deque()
            q.append([r, c])
            ocean.add((r, c))
            while q:
                row, col = q.popleft()
                for dr, dc in direction:
                    nr, nc = row + dr, col + dc
                    if 0 <= nr < rows and 0 <= nc < cols and not (nr, nc) in ocean and heights[row][col] <= heights[nr][nc]:
                        ocean.add((nr, nc))
                        q.append([nr, nc])
        for r, c in pacific:
            bfs(r, c, pac)
        for r, c in atlantic:
            bfs(r, c, atl)
        res = []

        for i in range(rows):
            for j in range(cols):
                if (i, j) in pac and (i, j) in atl:
                    res.append([i, j])
        return res
