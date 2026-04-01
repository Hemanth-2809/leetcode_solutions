import java.util.*;

class Solution {

    class Pair{
        int r;
        int c;

        Pair(int r,int c){
            this.r = r;
            this.c = c;
        }
    }

    public int[][] updateMatrix(int[][] mat) {

        int m = mat.length;
        int n = mat[0].length;

        Queue<Pair> q = new LinkedList<>();

        int[][] dist = new int[m][n];

        boolean[][] vis = new boolean[m][n];

        
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){

                if(mat[i][j]==0){
                    q.add(new Pair(i,j));
                    vis[i][j]=true;
                }
            }
        }

        int[][] dirs = {{1,0},{-1,0},{0,1},{0,-1}};

        while(!q.isEmpty()){

            Pair p = q.poll();

            int r = p.r;
            int c = p.c;

            for(int[] d:dirs){

                int nr = r+d[0];
                int nc = c+d[1];

                if(nr<0 || nc<0 || nr>=m || nc>=n)
                    continue;

                if(!vis[nr][nc]){

                    dist[nr][nc] = dist[r][c] + 1;

                    vis[nr][nc]=true;

                    q.add(new Pair(nr,nc));
                }
            }
        }

        return dist;
    }
}
