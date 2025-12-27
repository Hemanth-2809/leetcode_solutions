class Solution(object):
    def subsetXORSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
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
        
        
        total = 0
        for subset in res:
            xor_val = 0
            for x in subset:
                xor_val ^= x
            total += xor_val

        return total


          
        
