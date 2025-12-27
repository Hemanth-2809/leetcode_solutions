class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []

        def backtrack(start, remaining):
            if remaining == 0:
                res.append(path[:])
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i, remaining - candidates[i])
                path.pop()

        backtrack(0, target)
        return res
        
