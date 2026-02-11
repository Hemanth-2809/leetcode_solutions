class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = {}
        def f(amt):
            if amt == 0:
                return 0
            if amt in dp:
                return dp[amt]
            x = 1e9
            for c in coins:
                if amt-c >=0:
                    x = min(x,1+f(amt-c))
            dp[amt] = x
            return x
        ans = f(amount)
        if ans == 1e9:
            return -1
        return ans


        
