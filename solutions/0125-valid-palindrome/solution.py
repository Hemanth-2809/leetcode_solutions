class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result = ""
        for c in s:
            if c.isalnum():
                result += c.lower()

        for i in range((len(result)/2)):
            if result[i] != result[len(result)-1-i]:
                return False
        return True


        
