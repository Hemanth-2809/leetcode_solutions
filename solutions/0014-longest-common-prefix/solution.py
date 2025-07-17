class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        s = strs[0]
        for i in range(1,len(strs)):
            while s!="":
                if s == strs[i][:len(s)]:
                    break
                else:
                    s = s[:-1]

        return s            

             
