import heapq
class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """

        pending = []
        avl = []
        res = []
        time = 0
        for i,(etime,ptime) in enumerate(tasks) :
            heapq.heappush(pending,(etime,ptime,i))
            
        while pending or avl:
            while pending and pending[0][0]<=time:
                etime,ptime,j = heapq.heappop(pending)
                heapq.heappush(avl,(ptime,j))
               
            if avl:
                y = heapq.heappop(avl)
                time += y[0]
                res.append(y[1])
            else:
                time = pending[0][0]
        return res

        


        
