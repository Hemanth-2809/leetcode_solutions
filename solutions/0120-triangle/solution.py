class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n = len(triangle)
        dp = [[99999]*i for i in range(1,n+1)] 
        def f(i,j):
            if i==(n-1):
                return triangle[i][j]
            if dp[i][j] != 99999:
                return dp[i][j]
            dp[i][j] = min((triangle[i][j]+f(i+1,j)),(triangle[i][j]+f(i+1,j+1)))
            return dp[i][j]
        return f(0,0)
        
