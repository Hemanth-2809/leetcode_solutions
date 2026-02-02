class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(board)
        cols = len(board[0])
        def mark_u(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c]!="O":
                return
            board[r][c] = "U"
            mark_u(r+1,c)
            mark_u(r-1,c)
            mark_u(r,c+1)
            mark_u(r,c-1)
        for r in range(rows):
            if board[r][0] == "O":
                mark_u(r,0)
            if board[r][cols-1] == "O":
                mark_u(r,cols-1)
        for c in range(cols):
            if board[0][c] == "O":
                mark_u(0,c)
            if board[rows-1][c] == "O":
                mark_u(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "U":
                    board[r][c] ="O"
                

        


            
        



                    
                
                    
                    
            






        
