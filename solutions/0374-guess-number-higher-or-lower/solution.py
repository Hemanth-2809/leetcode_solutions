# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        h = n
        while l<=h:
            num = (l+h)//2
            if guess(num) == 0:
                return num
            elif guess(num) == -1:
                h = num-1
            else:
                l = num+1
        


        
