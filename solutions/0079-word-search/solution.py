class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board[0])
        n = len(board)
        Bool = [False]
        used = [[False for _ in range(m)] for _ in range(n)]
        def backtrack(i,j,l):
            if l == len(word):
                Bool[0] = True
                return 
            if i> 0 and board[i-1][j] == word[l] and not used[i-1][j]:
                used[i-1][j] = True 
                backtrack(i-1,j,l+1)
                used[i-1][j] = False

            if i+1<n and board[i+1][j] == word[l] and not used[i+1][j]:
                used[i+1][j] = True
                backtrack(i+1,j,l+1)
                used[i+1][j] = False

            if j>0 and board[i][j-1] == word[l] and not used[i][j-1]:
                used[i][j-1] = True
                backtrack(i,j-1,l+1)
                used[i][j-1] = False

            if j+1<m and board[i][j+1] == word[l] and not used[i][j+1]:
                used[i][j+1] = True
                backtrack(i,j+1,l+1)
                used[i][j+1] = False

            
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    used[i][j] = True
                    backtrack(i,j,1)
                    used[i][j] = False

        return Bool[0]
            
             
            
        
