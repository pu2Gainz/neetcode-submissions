class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        rows = len(grid)
        cols = len(grid[0])
        q = deque()
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append([i, j])
                if grid[i][j] == 1:
                    count += 1

        minute = 0
        if count == 0:
            return 0
        while q:
            qLen = len(q)
            minute += 1
            for i in range(qLen):
                r, c = q.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        count -= 1
                        q.append([nr, nc])
                
                if count == 0:
                    return minute
        
        return -1
