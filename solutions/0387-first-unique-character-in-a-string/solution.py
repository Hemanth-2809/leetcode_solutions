class Solution(object):
    def firstUniqChar(self, s):
        dict_1 = {}
        for ch in s:
           if ch in dict_1:
               dict_1[ch] += 1
           else:
               dict_1[ch] = 1

        for i in range(len(s)):
            if dict_1[s[i]] == 1:
               return i
        return -1
