class Solution(object):
    def largestSubmatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        maxx = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1 and 0<i:
                    matrix[i][j] = matrix[i-1][j]+1
            lis = sorted(matrix[i],reverse = True)

            for j in range(n):
                maxx = max((lis[j]*(j+1)),maxx)

       
        return maxx



        
