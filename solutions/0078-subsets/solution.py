class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        sol,res = [],[]
        def allsubsets(i):
            if i == n:
                res.append(sol[:])
                return

            allsubsets(i+1)

            sol.append(nums[i])
            allsubsets(i+1)
            sol.pop()
        allsubsets(0)
        
        return res
        
