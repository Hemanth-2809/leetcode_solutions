class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(grid)
        cols = len(grid[0])

        time = [0]
        fresh = [0]
        q = deque()

        # Initial scan
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh[0] += 1

        seen = [[False for _ in range(cols)] for _ in range(rows)]

        
        while q and fresh[0] > 0:
            size = len(q)
            for _ in range(size):
                ro, co = q.popleft()
                for dr, dc in dirs:
                    nr, nc = ro + dr, co + dc

                    if nr < 0 or nc < 0 or nr >= rows or nc >= cols:
                        continue
                    if grid[nr][nc] != 1 or seen[nr][nc]:
                        continue

                    seen[nr][nc] = True
                    grid[nr][nc] = 2
                    fresh[0] -= 1
                    q.append((nr, nc))

            time[0] += 1

        return time[0] if fresh[0] == 0 else -1

