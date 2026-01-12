# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: Optional[TreeNode]
        :type val: int
        :rtype: Optional[TreeNode]
        """
        x = TreeNode(val)
        if not root:
            return x
        def insert(node):

            if val < node.val:
                if node.left is None:
                    node.left = x
                else:
                    insert(node.left)
            else:
                if node.right is None:
                    node.right = x
                else:
                    insert(node.right)
        insert(root)
        return root

        
