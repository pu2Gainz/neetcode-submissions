class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        N = len(grid)
        if grid[0][0] or grid[N - 1][N - 1]:
            return -1

        directions = [[0, 1], [0, -1], [1, 0], [1, 1], [1, -1], [-1, 0], [-1, 1], [-1, -1]]

        q = deque([(0, 0)])
        grid[0][0] = 1

        while q:
            r, c = q.popleft()
            dist = grid[r][c]

            if r == N - 1 and c == N - 1:
                return dist
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < N and 0 <= nc < N and grid[nr][nc] == 0:
                    grid[nr][nc] = dist + 1
                    q.append((nr, nc))

        return -1
        