class Solution {
    private static final int[][] directions = {{1, 0}, {0, 1}, {-1, 0}, {0, -1}};

    public int numIslands(char[][] grid) {
        int count = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == '1') {
                    count += 1;
                    this.bfs(grid, r, c);
                }
            }
        }
        return count;
    }

    private void bfs(char[][] grid, int r, int c) {
        Queue<int[]> q = new ArrayDeque<>();

        grid[r][c] = '0';
        q.offer(new int[]{r, c});

        while (!q.isEmpty()) {
            int[] cell = q.poll();
            int row = cell[0];
            int col = cell[1];

            for (int[] direction : directions) {
                int nr = row + direction[0];
                int nc = col + direction[1];

                if (nr < 0 || nr >= grid.length || nc < 0 ||
                    nc >= grid[0].length || grid[nr][nc] == '0') continue;
                grid[nr][nc] = '0';
                q.offer(new int[]{nr, nc});
            }
        }

    }


}
