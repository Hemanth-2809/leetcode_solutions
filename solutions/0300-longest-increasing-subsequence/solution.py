class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        dp = [-1]*(n)
        def f(i):
            if dp[i] != -1:
                return dp[i]
            l = 1
            for j in range(i+1,n):
                if nums[i]<nums[j]:
                    l = max(l,1+f(j))
            dp[i] = l
            return l
        return max(f(i)for i in range(n))

