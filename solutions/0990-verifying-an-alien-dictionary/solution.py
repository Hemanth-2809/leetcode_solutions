class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        index = {order[i]:i for i in range(len(order))}
        for i in range(len(words)-1):
            w1,w2 = words[i],words[i+1]
            for j in range(len(w1)):
                if j == len(w2):
                    return False
                if w1[j] != w2[j]:
                    if index[w1[j]]>index[w2[j]]:
                        return False
                    break
        return True        
