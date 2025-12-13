class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        see = {0:1}
        count = 0 
        summ = 0 

        for i in range(len(nums)):
            summ = summ+nums[i]
            if summ-goal in see:
                count+=see[summ-goal]

            see[summ] = see.get(summ,0)+1
        return count

        
        
