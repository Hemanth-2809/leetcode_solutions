# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        ll = []
        def backtrack(node,d):
            if not node:
                return
            if len(ll)<=d:
                ll.append(node.val)
            backtrack(node.right,d+1)
            backtrack(node.left,d+1)
        backtrack(root,0)
        return ll
            

        
