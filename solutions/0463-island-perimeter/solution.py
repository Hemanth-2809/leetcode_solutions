from collections import deque
class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        p = 0
        q = deque()
        n = len(grid)
        m = len(grid[0])

        def find(grid):
            for j in range(n):
                for i in range(m):
                    if grid[j][i] == 1:
                        return (j,i)
        
        f = find(grid)
        q.append(f)
        seen = set([f])
        
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while q:
            j, i = q.popleft()
            x = 4

            for dj, di in dirs:
                nj, ni = j + dj, i + di

                if 0 <= nj < n and 0 <= ni < m and grid[nj][ni] == 1:
                    x -= 1
                    if (nj, ni) not in seen:
                        seen.add((nj, ni))
                        q.append((nj, ni))

            p += x


        return p

            




            
            

        




        
