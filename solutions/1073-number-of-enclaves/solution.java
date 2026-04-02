class Solution {
    int m,n;
    public int numEnclaves(int[][] grid) {
        m = grid.length;
         n = grid[0].length;

        for(int i = 0;i< m ;i++){
            if(grid[i][0] == 1){
                dfs(i,0,grid);
            }
            if(grid[i][n-1] == 1){
                dfs(i,n-1,grid);
            } 

        }
         for(int i = 0;i< n ;i++){
            if(grid[0][i] == 1){
                dfs(0,i,grid);
            }
            if(grid[m-1][i] == 1){
                dfs(m-1,i,grid);
            } 
            
        }
        int ans = 0;
        for(int i = 0;i<m;i++){
            for(int j = 0; j<n;j++){

                if(grid[i][j]==1){
                    ans+=1;
                }


            }

        }
        return ans;

        
        
    }
    public void dfs(int r,int c,int[][] grid){
        if(r<0 || r>=m || c<0 || c>=n || grid[r][c] != 1){
            return;
        }

        grid[r][c] = 0;

        dfs(r+1,c,grid);
        dfs(r-1,c,grid);
        dfs(r,c+1,grid);
        dfs(r,c-1,grid);
    }
}
