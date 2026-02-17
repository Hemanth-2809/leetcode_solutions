class Solution(object):
    def numDecodings(self, s):
        dp = {}

        def f(s):
            if len(s) == 0:
                return 1

            if s[0] == '0':
                return 0

            if s in dp:
                return dp[s]

            ways = f(s[1:])

            if len(s) >= 2 and 10 <= int(s[:2]) <= 26:
                ways += f(s[2:])

            dp[s] = ways
            return ways

        return f(s)
