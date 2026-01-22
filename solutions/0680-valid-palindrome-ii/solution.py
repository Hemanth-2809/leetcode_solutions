class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def fun(i,j):
            while i<j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            
            return True
        i = 0
        j = len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return (fun((i+1),j) or fun(i,(j-1)))
            i+=1
            j-=1
        return True

            
        
        
        


        
