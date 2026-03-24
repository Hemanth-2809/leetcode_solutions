class Solution(object):
    def constructProductMatrix(self, grid):

        n = len(grid)
        m = len(grid[0])
        MOD = 12345

        res = [[1]*m for _ in range(n)]

        prefix = 1

        for i in range(n):
            for j in range(m):
                res[i][j] = prefix
                prefix = (prefix * grid[i][j]) % MOD

        suffix = 1

        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                res[i][j] = (res[i][j] * suffix) % MOD
                suffix = (suffix * grid[i][j]) % MOD

        return res
