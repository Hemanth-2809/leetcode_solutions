class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        dp = [[-1]*(n) for _ in range(n)]
        def f(i,j):
            if i>j:
                return 0
            if i == j:
                return 1
            if dp[i][j] != -1:
                return dp[i][j]
            if s[i] == s[j]:
                dp[i][j] = f(i+1,j-1)+2
            else:
                dp[i][j] = max(f(i+1,j),f(i,j-1))
            return dp[i][j]
        return f(0,n-1)    
