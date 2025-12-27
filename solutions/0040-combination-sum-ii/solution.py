class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        sol , res = [],[] 
        n = len(candidates)

        def combos(i,remaining):
            if remaining == 0:
                res.append(sol[:])
                return
            if remaining < 0 or i == n:
                return

            sol.append(candidates[i])
            combos(i+1,(remaining-candidates[i]))
            sol.pop()

            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            combos(i + 1, remaining)
            


        
        combos(0,target)
        return res
        
        
        
        
