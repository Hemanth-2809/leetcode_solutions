class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        complete = 0
        l = 0
        h = n
        while l<=h:
            mid = (l+h)//2
            sum_num = (mid*(mid+1))/2
            if sum_num == n:
                return mid
            elif sum_num < n:
                complete = mid
                l = mid+1
            else:
                h = mid-1

        return complete
        
