class Solution {
    
    public List<Integer> eventualSafeNodes(int[][] graph) {
        int  n  = graph.length;
        int[] vis = new int[n];
        int[] path = new int[n];
        int[] check = new int[n];
        for(int i = 0;i<n;i++){
            if (vis[i] == 0){
                dfs(i,vis,path,graph,check);
            }
        }
        List <Integer> safe = new ArrayList<>();
        for(int i=0;i<n;i++){
            if (check[i] == 1){
                safe.add(i);
            }

        }
        return safe;


        
    }
    public boolean dfs(int node,int[] vis,int[] path,int[][] graph,int [] check){
        vis[node] = 1;
        path[node] = 1;
        for(int d:graph[node]){
            if(vis[d] == 0){
                if(dfs(d,vis,path,graph,check)== true){
                    return true;
                }
            }
            if(path[d] ==1){
                return true;
            }
        }
        path[node] = 0;
        check[node] = 1;
        return false; 

    }
}
