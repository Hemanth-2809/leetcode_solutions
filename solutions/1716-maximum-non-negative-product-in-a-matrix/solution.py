class Solution(object):
    def maxProductPath(self, grid):

        m = len(grid)
        n = len(grid[0])

        dp = [[[0,0] for j in range(n)] for i in range(m)]

        dp[0][0] = [grid[0][0],grid[0][0]]

        for i in range(1,m):
            dp[i][0][0] = dp[i-1][0][0]*grid[i][0]
            dp[i][0][1] = dp[i-1][0][1]*grid[i][0]

        for j in range(1,n):
            dp[0][j][0] = dp[0][j-1][0]*grid[0][j]
            dp[0][j][1] = dp[0][j-1][1]*grid[0][j]

        for i in range(1,m):
            for j in range(1,n):

                vals = [
                    dp[i-1][j][0]*grid[i][j],
                    dp[i-1][j][1]*grid[i][j],
                    dp[i][j-1][0]*grid[i][j],
                    dp[i][j-1][1]*grid[i][j]
                ]

                dp[i][j][0] = max(vals)
                dp[i][j][1] = min(vals)

        res = dp[m-1][n-1][0]

        if res < 0:
            return -1

        return res % (10**9+7)
