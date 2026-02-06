class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        mem = {}
        def climb(x):
            if x in mem:
                return mem[x]
            if x == 1:
                return 1
            if x == 2:
                return 2
            res = climb(x-1)+climb(x-2)
            mem[x] = res
            return res
        y = climb(n)
        return y


        
