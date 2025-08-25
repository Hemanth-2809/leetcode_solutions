class Solution(object):
    def maximumCandies(self, candies, k):
        """
        :type candies: List[int]
        :type k: int
        :rtype: int
        """
        l = 1
        r = max(candies)
        result = 0 
        while l<=r:
            mid = (l+r)//2
            count = 0
            for c in candies:
                count += c // mid
            if count >= k:
                result = mid
                l = mid+1
            else:
                r = mid-1
        return result

        
        
