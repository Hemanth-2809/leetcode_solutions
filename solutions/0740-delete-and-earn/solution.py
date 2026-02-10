class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = {}
        for num in nums:
            if num not in val:
                val[num]=0
            val[num]+=num
        nums = sorted(list(set(nums)))
        dp = [0]*(len(nums)+1)
        for i in range(len(nums)-1,-1,-1):
            ern = val[nums[i]]

            if i+1<len(nums) and nums[i]+1 == nums[i+1]:
                ern += dp[i+2]
            else:
                ern += dp[i+1]
            ern = max(ern,dp[i+1])
            dp[i] = ern
        return dp[0]

        
