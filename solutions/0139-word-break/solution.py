class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        
        dp = {}
        def f(i):
            if i == len(s):
                return True
            if i in dp:
                return dp[i]
            for w in wordDict:
                if s[i:i+len(w)] == w:
                    if f(i+len(w)):
                        dp[i] = True
                        return True
            dp[i] = False
            return False
        return f(0)

        
