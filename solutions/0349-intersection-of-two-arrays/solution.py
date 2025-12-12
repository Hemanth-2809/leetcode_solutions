class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        numm1 = set(nums1)
        numm2 = set(nums2)
        sol = []
        for x in numm1:
            if x in numm2:
                sol.append(x)
        return sol
        











        
