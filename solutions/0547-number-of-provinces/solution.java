import java.util.*;

class Solution {

    boolean[] visited;
    ArrayList<ArrayList<Integer>> adj;

    public int findCircleNum(int[][] isConnected) {
        
        int n = isConnected.length;

        visited = new boolean[n];

        adj = adjlist(isConnected);

        int ans = 0;

        for(int i = 0; i < n; i++){
            if(!visited[i]){
                ans++;
                dfs(i);
            }
        }

        return ans;
    }

    public ArrayList<ArrayList<Integer>> adjlist(int[][] isConnected){

        int n = isConnected.length;

        ArrayList<ArrayList<Integer>> adj = new ArrayList<>();

        for(int i = 0; i < n; i++){
            adj.add(new ArrayList<>());
        }

        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(isConnected[i][j] == 1 && i != j){
                    adj.get(i).add(j);
                }
            }
        }

        return adj;
    }

    public void dfs(int node){

        visited[node] = true;

        for(int neighbor : adj.get(node)){
            if(!visited[neighbor]){
                dfs(neighbor);
            }
        }
    }
}
