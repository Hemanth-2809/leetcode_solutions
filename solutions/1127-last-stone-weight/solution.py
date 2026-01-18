import heapq
class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        n_stones = [-x for x in stones]
        heapq.heapify(n_stones)
        while len(n_stones)>1:
            f = heapq.heappop(n_stones)
            s = heapq.heappop(n_stones)
            if s>f:
                heapq.heappush(n_stones,f-s)
        n_stones.append(0)
        return abs(n_stones[0])




        
