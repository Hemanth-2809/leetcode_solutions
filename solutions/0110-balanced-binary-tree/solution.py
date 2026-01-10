# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        res = [True]
        def backtrack(node):
            if not node:
                return 0
            
            left = backtrack(node.left)
            right = backtrack(node.right)
            if (max(left,right)-min(left,right)>1):
                res[0] = False
            return (1+max(left,right))
        backtrack(root)
        return res[0]

        
