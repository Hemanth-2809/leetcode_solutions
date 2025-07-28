class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack)):
            x = -1

            if haystack[i] == needle[0]:
                x = i
                for j in range(1,len(needle)):
                    if i+j < len(haystack) and haystack[i+j] == needle[j]:
                        pass
                    else:
                        x = -1
                        break
            if x == -1:
                continue
            else:
                break
                    
        return x
                



