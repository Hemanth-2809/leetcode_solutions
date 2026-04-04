import java.util.*;

class Solution {
    public boolean isBipartite(int[][] graph) {
        
        int n = graph.length;
        int[] col = new int[n];
        Arrays.fill(col, -1);

        for(int start = 0; start < n; start++){

            if(col[start] != -1) continue;

            Queue<Integer> q = new LinkedList<>();
            q.add(start);
            col[start] = 0;

            while(!q.isEmpty()){

                int node = q.poll();

                for(int d : graph[node]){

                    if(col[d] == -1){

                        col[d] = 1 - col[node]; 
                        q.add(d);
                    }
                    else if(col[d] == col[node]){
                        return false;
                    }
                }
            }
        }

        return true;
    }
}
