import java.util.*;

class Solution {

    class Pair {
        int r;
        int c;
        int distance;

        Pair(int i, int j, int d) {
            this.r = i;
            this.c = j;
            this.distance = d;
        }
    }

    public int dijkstra(int n, int[][] grid) {

        // If start or end is blocked
        if (grid[0][0] == 1 || grid[n - 1][n - 1] == 1) {
            return -1;
        }

        PriorityQueue<Pair> pq =
                new PriorityQueue<>((x, y) -> x.distance - y.distance);

        int[][] dist = new int[n][n];

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], (int) 1e9);
        }

        dist[0][0] = 1;
        pq.add(new Pair(0, 0, 1));

        int[][] dirs = {
                {1, 0}, {-1, 0}, {0, 1}, {0, -1},
                {1, 1}, {1, -1}, {-1, 1}, {-1, -1}
        };

        while (!pq.isEmpty()) {

            Pair curr = pq.poll();

            int i = curr.r;
            int j = curr.c;
            int dis = curr.distance;

            
            if (i == n - 1 && j == n - 1) {
                return dis;
            }

            for (int[] d : dirs) {

                int nr = i + d[0];
                int nc = j + d[1];

                
                if (nr < 0 || nc < 0 || nr >= n || nc >= n) {
                    continue;
                }

                
                if (grid[nr][nc] == 1) {
                    continue;
                }

                if (dis + 1 < dist[nr][nc]) {

                    dist[nr][nc] = dis + 1;

                    pq.add(new Pair(nr, nc, dist[nr][nc]));
                }
            }
        }

        return -1;
    }

    public int shortestPathBinaryMatrix(int[][] grid) {

        int n = grid.length;

        return dijkstra(n, grid);
    }
}
