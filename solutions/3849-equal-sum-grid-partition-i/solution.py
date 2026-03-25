class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        m = len(grid)
        n = len(grid[0])
        row = []
        col = [0]*n
        
        for i in range(m):
            summ = 0
            for j in range(n):
                summ += grid[i][j]
                col[j]+= grid[i][j]
            row.append(summ)
        total_summ = sum(row)
        if total_summ % 2 != 0:
            return False
        half = total_summ/2
        x = 0
        for i in range(m):
            x+=row[i]
            if x == half:
                return True
        y = 0
        for i in range(n):
            y+=col[i]
            if y == half:
                return True
        return False

            
        

