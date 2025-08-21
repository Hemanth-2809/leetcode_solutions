class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        n = len(matrix[0])
        l = 0 
        h = m-1
        right = n-1
        row = -1
        while l<=h:
            mid =(l+h)//2
            if matrix[mid][0] <= target<= matrix[mid][right]:
                row=mid
                break
            elif target < matrix[mid][0]:
                h = mid-1
                
            else:
                l = mid+1
        if row == -1:
            return False
        left = 0
        right = n-1
        while left<=right:
            mid = (left+right)//2
            if matrix[row][mid]==target:
                return True
            elif target < matrix[row][mid]:
                right = mid-1
            else:
                left = mid+1
        return False


        
