class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        p1 = 0  # Position to put next non-zero
        for p2 in range(len(nums)):
            if nums[p2] != 0:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p1 += 1

