class Solution(object):
    def subarraysDivByK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        see = {0:1}
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ%k in see:
                count+=see[summ%k]
            see[summ%k] =see.get(summ%k,0)+1
        return count


        
