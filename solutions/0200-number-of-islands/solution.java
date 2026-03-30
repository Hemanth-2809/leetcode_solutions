class Solution {

    public int numIslands(char[][] grid) {

        int m = grid.length;
        int n = grid[0].length;

        int ans = 0;

        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){

                if(grid[i][j] == '1'){
                    ans++;
                    bfs(i, j, grid);
                }
            }
        }

        return ans;
    }

    public void bfs(int i, int j, char[][] grid){

        int[][] dirs = {
            {1,0},
            {0,1},
            {-1,0},
            {0,-1}
        };

        grid[i][j] = '0';

        for(int[] d : dirs){

            int nr = i + d[0];
            int nc = j + d[1];

            if(nr < 0 || nc < 0 || nr >= grid.length || nc >= grid[0].length){
                continue;
            }

            if(grid[nr][nc] == '1'){
                bfs(nr, nc, grid);
            }
        }
    }
}
