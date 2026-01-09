# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res = [0]
        def backtrack(node,depth):
            if not node:
                return
            res[0] = max(res[0],depth)
            backtrack(node.left,depth+1)
            backtrack(node.right,depth+1)
        backtrack(root,1)
        return res[0]
            

        
