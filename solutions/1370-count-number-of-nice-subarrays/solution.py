class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        numodd = 0 
        see = {0:1}
        count = 0 
        for i in range(len(nums)):
            if nums[i]%2 != 0:
                numodd +=1
            if numodd - k in see:
                count+=see[numodd-k]
            see[numodd] = see.get(numodd,0)+1
        return count 
        
