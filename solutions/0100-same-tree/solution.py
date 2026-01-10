# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        res = [True]
        def backtrack(node1,node2):
            if not node1 and not node2:
                return
            if node1 is None or node2 is None:
                res[0] = False
                return
            if node1.val !=node2.val :
                res[0] = False
            backtrack(node1.left,node2.left)
            backtrack(node1.right,node2.right)
        backtrack(p,q)
        return res[0]
            

        
