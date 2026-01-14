# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        max_fornow = root.val
        count = [0]
        def backtrack(node,max_tillnow):
            if not node:
                return
            if node.val>=max_tillnow:
                count[0]+=1
                max_tillnow = node.val
            backtrack(node.right,max_tillnow)
            backtrack(node.left,max_tillnow)
        backtrack(root,max_fornow)
            
            
            
        return count[0]
            
            
        
