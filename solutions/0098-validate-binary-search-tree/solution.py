# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res = []
        def backtrack(node):
            if not node:
                return
            backtrack(node.left)
            res.append(node.val)
            backtrack(node.right)
        backtrack(root)
        n = len(res)
        for i in range(n):
            if i+1 <n and not res[i]< res[i+1]:
                return False
        return True

 
        
