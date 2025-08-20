class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        l = 1
        h = num
        while l<=h:
            mid = (l+h)//2
            if mid**2 == num:
                return True
            elif mid**2 > num:
                h = mid-1
            else:
                l = mid+1
        return False
        
        
