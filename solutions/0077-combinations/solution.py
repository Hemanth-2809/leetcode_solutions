class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        sol,res = [],[]
        
        def allcombinations(i):
            if len(sol) == k:
                res.append(sol[:])
                return
            

            for j in range(i,n+1):
                sol.append(j)
                allcombinations(j+1)
                sol.pop()
        allcombinations(1)
        return res
        
        



            
            
            
        
