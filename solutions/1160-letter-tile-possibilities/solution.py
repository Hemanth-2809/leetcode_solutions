class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        tiles = sorted(tiles)
        count = [0]
        n = len(tiles)
        sol = []
        used = [False]*n

        def backtrack():

            if len(sol)>0:
                count[0]+=1

            for i in range(n):
                if used[i]:
                    continue
                if i>0 and tiles[i] == tiles[i-1] and not used[i-1]:
                    continue
                    
                    
                used[i] = True
                sol.append(tiles[i])
                backtrack()
                sol.pop()
                used[i] = False
                     

        backtrack()
        return count[0]
            
        
       

            
