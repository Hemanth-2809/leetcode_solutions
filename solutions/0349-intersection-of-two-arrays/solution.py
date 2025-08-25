class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1.sort()
        nums2.sort()
        nums_intr = []
        i = 0
        j = 0
        while i < len(nums1)and j <len(nums2):
            if nums1[i] == nums2[j] :
                if nums1[i] not in nums_intr:
                    nums_intr.append(nums1[i])
                j+=1
                i+=1
            elif nums1[i] < nums2[j]:
                i +=1
            elif nums2[j] < nums1[i]:
                j+=1
        return nums_intr
        
