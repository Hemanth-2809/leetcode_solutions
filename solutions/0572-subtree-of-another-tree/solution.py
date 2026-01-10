# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
        res = [False]
        result = [False]
        def dfs(node):
            if not node:
                return
            if node.val == subRoot.val:
                res[0] = True
                x = backtrack(node,subRoot)
                if x:
                    result[0]= x
                
            dfs(node.left)
            dfs(node.right)


        
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
            return res[0]
        dfs(root)
        return result[0]
        


        
