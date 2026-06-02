class Solution {
    class pair{
        int node;
        long dist;
        pair(int n,long d){
            this.node = n;
            this.dist = d;
        }
    }
    public int dijkstra(int n,int[][] roads){
        List<List<int[]>> adj =  new ArrayList<>();
        for(int i = 0; i<n;i++){
            adj.add(new ArrayList<>());
        }
        for(int[] r: roads){
            int u = r[0];
            int v = r[1];
            int time = r[2];

            adj.get(u).add(new int[]{v,time});
            adj.get(v).add(new int[]{u,time});

        }
        PriorityQueue<pair> pq = new PriorityQueue<>((x,y)->Long.compare(x.dist,y.dist));
        pq.add(new pair(0,0));
        long[] dist = new long[n];
        Arrays.fill(dist,Long.MAX_VALUE);
        int[] ways = new int[n];
        Arrays.fill(ways, 0);
        dist[0] = 0;
        ways[0] = 1;
        int MOD = 1000000007;
        while(!pq.isEmpty()){
            pair curr = pq.poll();
            int currnode = curr.node;
            long currtime = curr.dist;
            if(curr.dist > dist[curr.node]) continue;
            for(int[] nei:adj.get(currnode)){
                int nxtnode = nei[0];
                int timetaken = nei[1];
                if(dist[nxtnode]>(currtime+timetaken)){
                    dist[nxtnode] = currtime+timetaken;
                    ways[nxtnode] = ways[currnode];
                    pq.add(new pair(nxtnode,dist[nxtnode]));
                }
                else if(dist[nxtnode] == currtime + timetaken){
                ways[nxtnode]= (ways[nxtnode]+ ways[currnode])%MOD;
                }
            }




        }
        return ways[n-1];


    }
    public int countPaths(int n, int[][] roads) {

        return dijkstra(n,roads);
        
    }
}
