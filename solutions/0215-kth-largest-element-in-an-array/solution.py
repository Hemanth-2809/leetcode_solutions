class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n_nums = [-x for x in nums]
        heapq.heapify(n_nums)
        
        for i in range(k):
            res = -(heapq.heappop(n_nums))
        return res
        
