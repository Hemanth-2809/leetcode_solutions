class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        n = len(nums)
        res,sol = [],[]
        used = [False]*len(nums)
        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i>0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue   
                used[i] = True
                sol.append(nums[i])
                backtrack()
                sol.pop()
                used[i]=False
        backtrack()
        return res
