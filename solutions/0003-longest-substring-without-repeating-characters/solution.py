class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_len = 0
        i = 0
        j = 1
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        dup = [s[i]]
        while i<len(s) and j < len(s):
            if s[j] in dup:
                dup.remove(s[i])
                i+=1
            else:
                dup.append(s[j])
                j+=1
            if max_len < len(dup):
                max_len = len(dup)
        return max_len
                
            


        
