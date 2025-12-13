class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        see = {0:1}
        count = 0 
        summ = 0 

        for i in range(len(nums)):
            summ = summ+nums[i]
            if summ-k in see:
                count+=see[summ-k]

            see[summ] = see.get(summ,0)+1
        return count

        
