class Solution(object):
    def pacificAtlantic(self, heights):
        """
        :type heights: List[List[int]]
        :rtype: List[List[int]]
        """
        dirs = [[1,0],[0,1],[-1,0],[0,-1]]
        rows = len(heights)
        cols = len(heights[0])
        p_cells = set()
        a_cells = set()
        res = []
        
        def dfs(r, c, visit, prevHeight):
            if ((r, c) in visit or
                r < 0 or c < 0 or
                r == rows or c == cols or
                heights[r][c] < prevHeight
            ):
                return
            visit.add((r, c))
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r - 1, c, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
        for i in range(rows): 
            dfs(i,0,p_cells,heights[i][0])
            dfs(i,cols-1,a_cells,heights[i][cols-1])
        for i in range(cols): 
            dfs(0,i,p_cells,heights[0][i])
            dfs(rows-1,i,a_cells,heights[rows-1][i])
        for r in range(rows):
            for c in range(cols):
                if (r,c) in p_cells and (r,c) in a_cells:
                    res.append([r,c])
        return res

        

            






        
