class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(grid)
        columns = len(grid[0])
        islands = 0
        def bfs(r,c):
            q = deque()
            q.append((r,c))
            grid[r][c] = "0"
            while q:
                ro,co = q.popleft()
                for dr,dc in dirs:
                    nr,nc = ro+dr,co+dc
                    if (nr<0 or nc < 0 or nr>=rows or nc >= columns or grid[nr][nc]=="0"):
                        continue
                    q.append((nr,nc))
                    grid[nr][nc] = "0"

        
        for ro in range(rows):
            for co in range(columns):
                if grid[ro][co] == "1":
                    bfs(ro,co)
                    islands +=1
        return islands

        
