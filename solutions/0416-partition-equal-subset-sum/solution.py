class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        x = sum(nums)
        if x %2 != 0:
            return False
        dp = {}
        def f(i,n):
            if n == 0:
                return True
            if i >= len(nums) or n < 0:
                return False
            if (i,n) in dp:
                return dp[(i,n)]
            
            t = f(i+1,n-nums[i])
            s = f(i+1,n)
   
            dp[(i,n)] = t or s
            return dp[(i,n)]
        return f(0,x/2)
            

        
        
