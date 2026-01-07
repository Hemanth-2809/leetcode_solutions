class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n = len(s)
        i = 0 
        j = n-1
        for i in range(n//2):
            temp = s[i]
            s[i] = s[j]
            s[j] = temp
            j=j-1
        return s



        
