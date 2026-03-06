class Solution(object):
    '''
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dp = {}
        def f(i):
            if i >= len(nums)-1:
                return True
            elif i in dp:
                return dp[i]
            else:
                
                for j in range(i+1,min(len(nums), i + nums[i] + 1)):
                    if f(j):
                        dp[i] = True
                        return True
                dp[i] = False
                return False
        return f(0)'''
        
    def canJump(self, nums):
        max_reach = 0

        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])

        return True
        
    
