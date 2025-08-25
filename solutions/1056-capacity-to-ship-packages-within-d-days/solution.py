class Solution(object):
    def shipWithinDays(self, weights, days):
        """
        :type weights: List[int]
        :type days: int
        :rtype: int
        """
        def canship(capacity):
            days_used = 1
            current_load = 0

            for w in weights:
                if current_load+w > capacity:
                    days_used+=1
                    current_load = 0
                current_load+=w
            return days_used<=days

        l = max(weights)
        r = sum(weights)
        k = r
        while l<=r:
            mid = (l+r)//2
            if canship(mid):
                k = mid
                r = mid-1
            else:
                l = mid+1
        return k

                
        
