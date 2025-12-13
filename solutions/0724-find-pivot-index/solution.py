class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        summlist = []
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            summlist.append(summ)
        for i in range(len(summlist)):
            if (summlist[i-1] if i>0 else 0) == summlist[-1]-summlist[i]:
                return i
        return -1

            

        
