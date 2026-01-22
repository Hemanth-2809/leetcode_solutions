import heapq
class Solution(object):
    def longestDiverseString(self, a, b, c):
        """
        :type a: int
        :type b: int
        :type c: int
        :rtype: str
        """
        res = ""
        freq = []
        if a>0:
            heapq.heappush(freq,(-a,"a"))
        if b>0:
            heapq.heappush(freq,(-b,"b"))
        if c>0:
            heapq.heappush(freq,(-c,"c"))
        while freq:
            c1,ch1 = heapq.heappop(freq)
            if len(res)>1 and res[-1]==res[-2]==ch1:
                if not freq:
                    break
                c2,ch2 = heapq.heappop(freq)
                res+=ch2
                c2+=1
                if c2:
                    heapq.heappush(freq,(c2,ch2))
                heapq.heappush(freq,(c1,ch1))
            else:
                res+=ch1
                c1+=1
                if c1:
                    heapq.heappush(freq,(c1,ch1))

        return res


            

            




        
        
