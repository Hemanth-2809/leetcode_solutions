import math
class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """
        potions.sort()
        res = []
        for i in range(len(spells)):
            x = (success + spells[i] - 1) // spells[i]
            l = 0
            h = len(potions)
            while l<h:
                mid = (l+h)//2
                if potions[mid] < x:
                    l= mid+1
                else:
                    h = mid
            res.append(len(potions)-l)
        return res
            
        
        
