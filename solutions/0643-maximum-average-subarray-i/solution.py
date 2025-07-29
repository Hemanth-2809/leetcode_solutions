class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sums = sum(nums[:k])
        max_sum = sums

        
        for i in range(k,len(nums)):
            
            sums = sums + nums[i] - nums[i-k]
            if max_sum < sums:
                max_sum = sums
        return (max_sum/float(k)) 
        
