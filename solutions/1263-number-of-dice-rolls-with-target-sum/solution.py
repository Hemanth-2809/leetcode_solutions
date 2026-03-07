class Solution(object):
    def numRollsToTarget(self, n, k, target):
        """
        :type n: int
        :type k: int
        :type target: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = {}
        def f(nd,t):
            if nd == 0:
                return 1 if t == 0 else 0
            if (nd,t) in dp:
                return dp[(nd,t)]
            res = 0
            for i in range(1,k+1):
                if t - i>=0:
                    res = (res+f(nd-1,t-i))%MOD
            dp[(nd,t)] = res
            return res
        return f(n,target)
        
