class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <=3:
            return max(nums)
        nums_fir = nums[:n-1]
        nums_las = nums[1:n]

        dp_fir = [-1]*(n-1)
        dp_las = [-1]*(n-1)
        def f(n,nums,dp):
            if n==0:
                return nums[0]
            if n==1:
                return max(nums[0],nums[1])
            if dp[n]!=-1:
                return dp[n]
            dp[n] = max(f(n-1,nums,dp),(nums[n]+f(n-2,nums,dp)))
            return dp[n]
        return max(f(n-2,nums_fir,dp_fir),f(n-2,nums_las,dp_las))
        
