# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        res1 = [0]
        def backtrack(node):
            if not node:
                return 0

    
            left = backtrack(node.left)
            right = backtrack(node.right)
            res1[0] = max(res1[0],left+right)

            return (1+max(left,right))
        
        
        backtrack(root)
        



        return res1[0]




        
