class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        count = 0
        summ=sum(arr[0:k])
        for i in range(len(arr)-k+1):
            if summ/k >= threshold:
                count+=1
            if i+k < len(arr):
                summ = summ - arr[i]+arr[i+k]
        return count

        
