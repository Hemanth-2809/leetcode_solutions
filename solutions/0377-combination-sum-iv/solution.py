class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = {}
        def f(n):
            if n== 0:
                return 1
            if n in dp:
                return dp[n]
            res = 0
            for i in range(len(nums)):
                if n-nums[i] >= 0:
                    res = res + f(n-nums[i])
            dp[n] = res
            return res
        return f(target)
        
