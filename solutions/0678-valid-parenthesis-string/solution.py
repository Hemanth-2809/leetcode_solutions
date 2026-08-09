class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        low = 0
        high = 0
        for x in s:
            if x =="(":
                low+=1
                high+=1
            elif x == ")":
                low-=1
                high-=1
            else:
                low-=1
                high+=1
            low = max(0,low)
            if high<0:
                return False
        return low == 0
        
            

