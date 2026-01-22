import heapq
class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        filled = 0
        s_trips = []
        dest = []
        res = True
        for i in range(len(trips)):
            heapq.heappush(s_trips,(trips[i][1],trips[i][2],trips[i][0]))
        while s_trips:
            fromi,toi_now,pas_now = heapq.heappop(s_trips)
            heapq.heappush(dest,(toi_now,pas_now))
            toi,pas = heapq.heappop(dest)
            while dest and toi<=fromi:
                filled -= pas
                toi,pas = heapq.heappop(dest)
            heapq.heappush(dest,(toi,pas))
            if (filled+pas_now)>capacity:
                return False
            else:
                filled+=pas_now


        return res
            





           
                



        

        
