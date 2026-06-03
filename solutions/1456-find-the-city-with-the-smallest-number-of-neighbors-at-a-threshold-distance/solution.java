class Solution {
    public int bellman(int n, int[][] edges, int dt) {

        int[][] distarr = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(distarr[i], Integer.MAX_VALUE);
        }
        int[] thresh = new int[n];
        for (int i = 0; i < n; i++) {
            distarr[i][i] = 0;
            for (int j = 0; j < n; j++) {
                for (int[] ed : edges) {
                    int u = ed[0];
                    int v = ed[1];
                    int dis = ed[2];
                    if (distarr[i][u] != Integer.MAX_VALUE && distarr[i][u] + dis < distarr[i][v]) {
                        distarr[i][v] = distarr[i][u] + dis;

                    }
                    if (distarr[i][v] != Integer.MAX_VALUE && distarr[i][v] + dis < distarr[i][u]) {
                        distarr[i][u] = distarr[i][v] + dis;// as birectional
                    }

                }

            }

        }
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (i != j && distarr[i][j] <= dt) {
                    thresh[i]++;
                }
            }
        }
        int ans = 0;
        for(int i= 0;i<n;i++){
            if(thresh[i]<= thresh[ans]){
                ans = i;
            }
        }
        return ans;

    }

    public int findTheCity(int n, int[][] edges, int distanceThreshold) {

    return bellman(n,edges,distanceThreshold);
}
}
