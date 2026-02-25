class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = {}
        def f(n):
            if n == 1:
                return 1
            if n in dp:
                return dp[n]
            
            val = 0
            for i in range(1,n):
                val = max(val,max(i,f(i))*max(n-i,f(n-i)))
            dp[n] = val
            return val
        return f(n)
        
        
