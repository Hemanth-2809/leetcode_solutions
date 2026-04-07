class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] adj = new ArrayList[numCourses];

        for(int i=0;i<numCourses;i++){
            adj[i] = new ArrayList<>();
        }

        for(int i=0;i<prerequisites.length;i++){
            adj[prerequisites[i][1]].add(prerequisites[i][0]);
        }
        Stack<Integer> order = new Stack<>();

        int[] vis = new int[numCourses];
        int[] path = new int[numCourses];

        for(int i=0;i<numCourses;i++){
            if(vis[i]==0){
                if(dfs(i,vis,path,adj,order)){
                    return new int[0];
                }
            }
        }
        int[] ans = new int[numCourses];
        int i = 0;

        while(!order.isEmpty()){
            ans[i] = order.peek();
            order.pop();
            i++;


        }
        return ans;
        
    }
    public boolean dfs(int node,int[] vis,int[] path,List<Integer>[] adj,Stack<Integer> order){

        vis[node] = 1;
        path[node] = 1;

        for(int neigh : adj[node]){

            if(vis[neigh]==0){
                if(dfs(neigh,vis,path,adj,order)){
                    return true;
                }
            }

            else if(path[neigh]==1){
                return true;
            }
        }

        path[node] = 0;
        order.push(node);


        return false;
    }


}

