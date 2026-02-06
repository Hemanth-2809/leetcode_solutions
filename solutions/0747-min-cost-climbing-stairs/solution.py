class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n =  len(cost)
        dpp = [-1]*n

        def dp(i):
            if i == 0:
                return cost[0]
            if i == 1:
                return cost[1]
            if dpp[i]!= -1:
                return dpp[i]
            dpp[i] = cost[i]+min(dp(i-1),dp(i-2))
            return dpp[i]
        return min(dp(n-1),dp(n-2))

            
        
