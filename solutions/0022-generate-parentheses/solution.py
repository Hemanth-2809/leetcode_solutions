class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        left = 0
        ryt =  0
        res,sol = [],[]

        def backtrack(left,ryt):
            if len(sol)==2*n:
                res.append("".join(sol))
                return
            
            
            if left < n:
                sol.append("(")
                backtrack(left+1,ryt)
                sol.pop()
            if ryt < left:
                sol.append(")")
                backtrack(left,ryt+1)
                sol.pop()
        backtrack(0,0)    
        return res
    """
    class Solution: 
    def generateParenthesis(self, n):
        res = []
        def backtrack(s, open, close):
            if len(s) == 2 * n:
                res.append(s)
                return
            if open < n:
                backtrack(s + "(", open + 1, close)
            if close < open:
                backtrack(s + ")", open, close + 1)
        backtrack("", 0, 0)
        return res        
    """
    
            
            

        

        
