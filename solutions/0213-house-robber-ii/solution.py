class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 3:
            return max(nums)
        dp1= [-1]*(n-1)
        dp2= [-1]*(n-1)
        num1 = nums[:n-1]
        num2 = nums[1:n]
        dp1[0] = num1[0]
        dp2[0] = num2[0]
   

        def f(i,dp,arr):
            if i < 0:
                return 0
            if i == 0:
                return arr[0]
            if dp[i] != -1:
                return dp[i]
            dp [i] = max((arr[i]+f(i-2,dp,arr)),f(i-1,dp,arr))
            return dp[i]
        
    
        return max(f(n-2,dp1,num1),f(n-2,dp2,num2))

        
