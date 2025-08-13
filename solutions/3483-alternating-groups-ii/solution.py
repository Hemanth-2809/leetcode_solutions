class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        """
        :type colors: List[int]
        :type k: int
        :rtype: int
        """
        arr = colors+colors[:k-1]
        left = 0
        right = 1
        result = 0 
        
        for right in range(1,len(arr)):
            if arr[right] == arr[right-1]:
                left = right 
            
            if right - left +1 >= k:
                left +=1
                result+=1
        return result

        
