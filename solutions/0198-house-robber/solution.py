class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1]*n
        def f(n):
            if n==0:
                return nums[0]
            if n==1:
                return max(nums[0],nums[1])
            if dp[n]!=-1:
                return dp[n]
            dp[n] = max(f(n-1),(nums[n]+f(n-2)))
            return dp[n]
        return f(n-1)
        
