class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        n = max(piles)
        
        l = 1
        r = n
        k = n
        while l<=r:
            
            hrs =0
            mid = (l+r)//2
            for p in piles:
                hrs += (p+mid-1)//mid
            
            if hrs <= h:
                k = mid
                r = mid-1
            elif hrs > h:
                l = mid+1
        return k





        
