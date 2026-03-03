class Solution(object):
    def bagOfTokensScore(self, tokens, power):
        """
        :type tokens: List[int]
        :type power: int
        :rtype: int
        """
        t = sorted(tokens)
        i = 0
        score = 0
        max_so = 0

        j = len(t)-1
        while i<=j:
            if t[i] <= power:
                score+=1
                max_so = max(max_so,score)
                power -= t[i]
                i+=1
                
            elif score > 0:
                power+=t[j]
                j-=1
                score-=1
            else:
                break
            
        return max_so
            



        
