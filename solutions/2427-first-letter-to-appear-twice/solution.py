class Solution(object):
    def repeatedCharacter(self, s):
        """
        :type s: str
        :rtype: str
        """
        dict_1 = {}
        for c in s:
            if c in dict_1:
                dict_1[c]+=1
            else:
                dict_1[c] = 1
            if dict_1[c] >=2:
                return c
        
        return 0
        
