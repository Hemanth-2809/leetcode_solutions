
import heapq
class Solution(object):
    def reorganizeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        freq = {}
        for char in s:
            if char.isalpha():
                freq[char] = freq.get(char, 0) + 1
        let = []
        for ch,c  in freq.items():
            heapq.heappush(let,(-c,ch))
        if -(let[0][0])>((len(s)+1)//2):
            return ""
        while len(let)>1:

            c1,ch1 = heapq.heappop(let)
            c2,ch2 = heapq.heappop(let)
            res = res+ch1+ch2
            c1 +=1
            c2 +=1
            if -c1 > 0:
                heapq.heappush(let,(c1,ch1))
            if -c2 > 0:
                heapq.heappush(let,(c2,ch2))
        if let:
            res+=let[0][1]
            
        return res
        
