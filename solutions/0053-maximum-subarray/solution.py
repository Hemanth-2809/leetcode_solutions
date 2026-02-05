class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_so_far = nums[0]
        curr_summ = nums[0]


        for i in range(1,len(nums)):
            curr_summ = max(nums[i],curr_summ+nums[i])
            max_so_far = max(curr_summ,max_so_far)
        return max_so_far
        
        
