class Solution(object):
    def maxIceCream(self, costs, coins):
        """
        :type costs: List[int]
        :type coins: int
        :rtype: int
        """
        c = sorted(costs)
        num =0
        for x in c:
            if x<=coins:
                num+=1
                coins-=x
        return num
        
