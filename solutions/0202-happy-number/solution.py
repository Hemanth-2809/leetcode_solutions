class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def next_num(x):
            total = 0
            while x > 0:
                digi = x % 10
                total+= digi*digi
                x = x//10
            return total
        see =set()
        while n!=1 and n not in see:
            see.add(n)
            n = next_num(n)
        if n == 1:
            return True
        else:
            return False

        
