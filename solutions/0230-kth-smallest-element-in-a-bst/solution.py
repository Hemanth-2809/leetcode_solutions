# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: Optional[TreeNode]
        :type k: int
        :rtype: int
        """
        res = []
        def backtrack(node):
            if not node:
                return
            backtrack(node.left)
            res.append(node.val)
            backtrack(node.right)
        backtrack(root)
        return res[k-1]
        
