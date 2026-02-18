class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        currmin = nums[0]
        currmax = nums[0]
        max_tillnow = nums[0]
        for i in range(1,len(nums)):
            num = nums[i]
            temp = currmax*num
            currmax = max(num,(currmin*num),(currmax*num))
            currmin = min(num,(currmin*num),temp)
            max_tillnow = max(max_tillnow,currmax)
        return max_tillnow



