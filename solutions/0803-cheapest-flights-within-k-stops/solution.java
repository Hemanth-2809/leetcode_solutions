import java.util.*;

class Solution {

    class Pair {
        int node;
        int cost;
        int stops;

        Pair(int node, int cost, int stops) {
            this.node = node;
            this.cost = cost;
            this.stops = stops;
        }
    }

    public int findCheapestPrice(int n, int[][] flights,
                                 int src, int dst, int k) {

        ArrayList<ArrayList<int[]>> adj = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            adj.add(new ArrayList<>());
        }

        for (int[] flight : flights) {
            int u = flight[0];
            int v = flight[1];
            int price = flight[2];

            adj.get(u).add(new int[]{v, price});
        }

        int[] dist = new int[n];
        Arrays.fill(dist, (int)1e9);

        Queue<Pair> q = new LinkedList<>();

        q.offer(new Pair(src, 0, 0));
        dist[src] = 0;

        while (!q.isEmpty()) {

            Pair curr = q.poll();

            int node = curr.node;
            int cost = curr.cost;
            int stops = curr.stops;

            
            if (stops > k) {
                continue;
            }

            for (int[] neighbour : adj.get(node)) {

                int nextNode = neighbour[0];
                int edgeCost = neighbour[1];

                if (cost + edgeCost < dist[nextNode]) {

                    dist[nextNode] = cost + edgeCost;

                    q.offer(
                        new Pair(
                            nextNode,
                            dist[nextNode],
                            stops + 1
                        )
                    );
                }
            }
        }

        return dist[dst] == (int)1e9 ? -1 : dist[dst];
    }
}
