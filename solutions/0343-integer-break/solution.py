class Solution(object):
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp ={}
        def f(num):
            if num == 1:
                return 1
            if num in dp:
                return dp[num]
            dp[num] = 0 if num == n else num
            for i in range(1, num):
                val = f(i) * f(num - i)
                dp[num] = max(dp[num], val)
            return dp[num]
        return f(n)

        
