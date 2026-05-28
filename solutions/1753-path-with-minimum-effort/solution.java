import java.util.*;

class Solution {

    class Pair {
        int r;
        int c;
        int effort;

        Pair(int r, int c, int effort) {
            this.r = r;
            this.c = c;
            this.effort = effort;
        }
    }

    public int minimumEffortPath(int[][] heights) {

        int n = heights.length;
        int m = heights[0].length;

        int[][] dist = new int[n][m];

        for (int i = 0; i < n; i++) {
            Arrays.fill(dist[i], (int)1e9);
        }

        PriorityQueue<Pair> pq =
                new PriorityQueue<>((x, y) -> x.effort - y.effort);

        dist[0][0] = 0;

        pq.add(new Pair(0, 0, 0));

        int[][] dirs = {
                {1, 0},
                {-1, 0},
                {0, 1},
                {0, -1}
        };

        while (!pq.isEmpty()) {

            Pair curr = pq.poll();

            int r = curr.r;
            int c = curr.c;
            int effort = curr.effort;

            
            if (r == n - 1 && c == m - 1) {
                return effort;
            }

            for (int[] d : dirs) {

                int nr = r + d[0];
                int nc = c + d[1];

                
                if (nr < 0 || nc < 0 || nr >= n || nc >= m) {
                    continue;
                }

                int newEffort = Math.max(
                        effort,
                        Math.abs(heights[nr][nc] - heights[r][c])
                );

                if (newEffort < dist[nr][nc]) {

                    dist[nr][nc] = newEffort;

                    pq.add(new Pair(nr, nc, newEffort));
                }
            }
        }

        return 0;
    }
}
