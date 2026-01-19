import math
import heapq
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        dist = []
        for x,y in points:
            z = (x**2+y**2)
            dist.append([z,x,y])


        heapq.heapify(dist)
        res = []
        for i in range(k):
            z,x,y = heapq.heappop(dist)
            res.append([x,y])
        return res



        
        
