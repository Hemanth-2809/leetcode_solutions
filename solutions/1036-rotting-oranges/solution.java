import java.util.*;

class Solution {
    public int orangesRotting(int[][] grid) {
        
        int m = grid.length;
        int n = grid[0].length;
        
        Deque<int[]> q = new ArrayDeque<>();
        
        int fresh = 0;
        int time = 0;
        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                
                if(grid[i][j]==2){
                    q.add(new int[]{i,j});
                }
                
                if(grid[i][j]==1){
                    fresh++;
                }
            }
        }
        
        if(fresh==0) return 0;
        
        int dirs[][]={{1,0},{-1,0},{0,1},{0,-1}};
        
        while(!q.isEmpty()){
            
            int size = q.size();
            boolean rotted = false;
            
            for(int k=0;k<size;k++){
                
                int cur[] = q.poll();
                
                for(int d[]:dirs){
                    
                    int nr = cur[0]+d[0];
                    int nc = cur[1]+d[1];
                    
                    if(nr<0 || nc<0 || nr>=m || nc>=n){
                        continue;
                    }
                    
                    if(grid[nr][nc]==1){
                        
                        grid[nr][nc]=2;
                        fresh--;
                        rotted = true;
                        
                        q.add(new int[]{nr,nc});
                    }
                }
            }
            
            if(rotted) time++;
        }
        
        if(fresh>0) return -1;
        
        return time;
    }
}
