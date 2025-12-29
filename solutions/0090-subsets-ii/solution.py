class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res,sol = [],[]
        def subsets(start):
            res.append(sol[:])

            for i in range(start,len(nums)):
                if i>start and nums[i] == nums[i-1]:
                    continue
                sol.append(nums[i])
                subsets(i+1)
                sol.pop()

        subsets(0)
        return res

        
