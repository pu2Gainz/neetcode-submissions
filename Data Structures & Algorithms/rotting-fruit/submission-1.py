class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()
        fresh = 0
        # add all rotten fruit into q
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1
        if fresh == 0:
            return 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        mins = -1
        while q:
            # add fruit to cell by neighbor
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc
                    if(0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        q.append((nr, nc))
                        fresh -= 1

            mins += 1

        return mins if fresh == 0 else -1





        