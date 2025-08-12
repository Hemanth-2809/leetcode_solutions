class Solution(object):
    def minimumDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if len(nums)==1:
            return 0
        nums.sort(reverse=True)
        min_diff = 9999999999
        for i in range(len(nums)-k+1):
            if nums[i]-nums[i+k-1]<min_diff:
                min_diff = nums[i]-nums[i+k-1]

        return min_diff
                
            



        return 
        
