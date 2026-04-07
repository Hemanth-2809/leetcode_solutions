class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {

        List<Integer>[] adj = new ArrayList[numCourses];

        for(int i=0;i<numCourses;i++){
            adj[i] = new ArrayList<>();
        }

        for(int i=0;i<prerequisites.length;i++){
            adj[prerequisites[i][1]].add(prerequisites[i][0]);
        }

        int[] vis = new int[numCourses];
        int[] path = new int[numCourses];

        for(int i=0;i<numCourses;i++){
            if(vis[i]==0){
                if(dfs(i,vis,path,adj)){
                    return false;
                }
            }
        }

        return true;
    }

    public boolean dfs(int node,int[] vis,int[] path,List<Integer>[] adj){

        vis[node] = 1;
        path[node] = 1;

        for(int neigh : adj[node]){

            if(vis[neigh]==0){
                if(dfs(neigh,vis,path,adj)){
                    return true;
                }
            }

            else if(path[neigh]==1){
                return true;
            }
        }

        path[node] = 0;

        return false;
    }
}
