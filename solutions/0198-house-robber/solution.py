class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1]*n
        dp[0] = nums[0]
        def f(i):
            if i <0:
                return 0
            if i == 0:
                return nums[0]
            if dp[i] != -1:
                return dp[i]
            dp [i] = max((nums[i]+f(i-2)),f(i-1))
            return dp[i]
        f(n-1)
        return dp[n-1]

        
