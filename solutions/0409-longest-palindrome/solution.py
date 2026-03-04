class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = {}
        for x in s:
            if x in dic:
                dic[x]+=1
            else:
                dic[x] =1
        center =0
        length = 0
        for f in dic.values():
            length += (f // 2) * 2
            if f % 2 == 1:
                center = True

        if center:
            length += 1
        return length

        
