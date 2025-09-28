class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(set(nums))
        if len(nums)== 0:
            return 0
        longest = 1
        counter = 1
        for i in range(1,len(nums)):
            
            if nums[i] == nums[i-1]+1:
                counter +=1
            else:
                longest = max(longest,counter)
                counter =1
        return max(longest,counter)

