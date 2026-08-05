class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g=sorted(g,reverse = True)
        s =sorted(s,reverse = True)
        i = 0
        ans = 0
        j = 0
        while i <len(s) and j<len(g):
            if s[i]>=g[j]:
                ans+=1
                i+=1
                j+=1

            else:
                j+=1
        return ans
        
