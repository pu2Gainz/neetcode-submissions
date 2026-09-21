class Solution {
    public void islandsAndTreasure(int[][] grid) {
        int inf = 2147483647;
        int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        int rows = grid.length;
        int cols = grid[0].length;

        Queue<int[]> queue = new ArrayDeque<>();

        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == 0) {
                    queue.offer(new int[]{r, c});
                }
            }
        }
        int dist = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            dist++;
            for (int i = 0; i < size; i++) {
                int[] cell = queue.poll();
                for (int[] dir : directions) {
                    int nr = cell[0] + dir[0];
                    int nc = cell[1] + dir[1];

                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] != inf) continue;
                    grid[nr][nc] = dist;
                    queue.offer(new int[]{nr, nc});
                }
            }
        }
    }
}
