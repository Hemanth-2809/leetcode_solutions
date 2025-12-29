class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res,sol = [],[]
        used = []
        def solution():
            if len(sol) == len(nums):
                res.append(sol[:])
                return
            for i in range(len(nums)):
                if nums[i] in used:
                    continue
                used.append(nums[i])
                sol.append(nums[i])
                solution()
                sol.pop()
                used.pop()
        solution()
        return res
