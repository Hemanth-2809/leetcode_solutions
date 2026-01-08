# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        res = []
        def preorder(node):
            if not node:
                return
            preorder(node.left)
            preorder(node.right)
            res.append(node.val)
        preorder(root)
        return res
        
