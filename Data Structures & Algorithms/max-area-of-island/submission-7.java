class Solution {
    private static final int[][] directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

    public int maxAreaOfIsland(int[][] grid) {
        int maxArea = 0;
        for (int r = 0; r < grid.length; r++) {
            for (int c = 0; c < grid[0].length; c++) {
                if (grid[r][c] == 1) {
                    maxArea = Math.max(maxArea, this.dfs(grid, r, c));
                }
            }
        }

        return maxArea;
    }

    private int dfs(int[][] grid, int r, int c) {
        if (r < 0 || r >= grid.length || c < 0 || c >= grid[0].length || 
            grid[r][c] == 0 ) return 0;
        
        grid[r][c] = 0;
        int area = 1;
        for (int[] direction : directions) {
            int nr = r + direction[0];
            int nc = c + direction[1];
            area += this.dfs(grid, nr, nc);
        }
        return area;
    }


}
