class Solution {
    public int floyd(int n, int[][] edges, int distanceThreshold) {
        int dist[][] = new int[n][n];
        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], Integer.MAX_VALUE);
            dist[i][i] = 0;

        }
        for (int[] edge : edges) {
            int u = edge[0];
            int v = edge[1];
            int w = edge[2];

            dist[u][v] = w;
            dist[v][u] = w;
        }

        int[] thresh = new int[n];
        for (int via = 0; via < n; via++) {
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (dist[i][via] == Integer.MAX_VALUE || dist[via][j] == Integer.MAX_VALUE) {
                        continue;
                    }
                    dist[i][j] = Math.min(dist[i][j], dist[i][via] + dist[via][j]);

                }
            }
        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && dist[i][j] <=distanceThreshold) {
                    thresh[i]++;
                }
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            if (thresh[i] <= thresh[ans]) {
                ans = i;
            }
        }
        return ans;

    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {
        return floyd(n, edges, distanceThreshold);

    }
}

