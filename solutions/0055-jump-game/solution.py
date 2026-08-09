class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dist = 0
        n = len(nums)
        for i in range(n):
            nums[i]= nums[i]+i
        nums[n-1] = n-1

        i =0
        while i <= dist:
            dist = max(nums[i],dist)

            i+=1
            if dist >= n-1:
                return True

        return False


