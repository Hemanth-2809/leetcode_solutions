class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        see = {}
        for word in strs:
            strr = ''.join(sorted(word))
            if strr in see:
                see[strr].append(word)
            else:
                see[strr] = [word]
        return list(see.values())

        
