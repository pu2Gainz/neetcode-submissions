class Solution {
    public int islandPerimeter(int[][] grid) {
        int rows = grid.length; 
        int cols = grid[0].length;
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        boolean[][] visited = new boolean[rows][cols];

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (visited[i][j]) continue;
                ArrayDeque<int[]> queue = new ArrayDeque<>();

                if (grid[i][j] == 1) {
                    queue.offer(new int[]{i, j});
                    visited[i][j] = true;

                    int parameter = 0;
                    while (!queue.isEmpty()) {
                        int[] cord = queue.poll();
                        int r = cord[0];
                        int c = cord[1];

                        for (int[] dir: directions) {
                            int nr = r + dir[0];
                            int nc = c+ dir[1];

                            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] == 0) {
                                parameter++;
                            } else if (visited[nr][nc]) {
                                continue;
                            } else {
                                visited[nr][nc] = true;
                                queue.offer(new int[]{nr, nc});
                            }
                        }
                    }
                    return parameter;
                }
                
            }
        }
        return 0;
    }
}