class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[-1]*n for _ in range(m)]
        dp[0][0] = grid[0][0]
        def f(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return float('inf')
            if i ==0 and j ==0:
                return grid[0][0]
            if dp[i][j] != -1:
                return dp[i][j]
            top = f(i-1,j)
            left = f(i,j-1)
            dp[i][j] = grid[i][j]+min(top,left)
            return dp[i][j]

        
        return f(m-1,n-1)












        

        
