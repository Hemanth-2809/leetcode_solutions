class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        min_recolor = 99999
        ch = 'W'
        for i in range(len(blocks)-k+1):
            count_w = blocks[i:i+k].count(ch)
            if min_recolor > count_w:
                min_recolor = count_w
        return min_recolor


        
