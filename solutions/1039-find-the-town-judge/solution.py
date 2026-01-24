class Solution(object):
    def findJudge(self, n, trust):
        """
        :type n: int
        :type trust: List[List[int]]
        :rtype: int
        """
        matrix =[[0 for _ in range(n)] for _ in range(n)]
        matrix_h =[[0 for _ in range(n)] for _ in range(n)]
        for i in range(len(trust)):
            x,y = trust[i][0]-1,trust[i][1]-1
            matrix[y][x] = 1
            matrix_h[x][y] = 1

            
        for i in range(len(matrix)):
            if (sum(matrix[i])==(n-1) and sum(matrix_h[i])==0):
                return i+1

        return -1
        

        
