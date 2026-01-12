# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        pp = []
        pq = []
        def path(node,x,ll):
            if not node:
                return
            ll.append(node)
            if node.val == x.val:
                return
            
            if x.val<node.val:
                path(node.left,x,ll)
            else:
                path(node.right,x,ll)
        path(root,p,pp)
        path(root,q,pq)
        
        def common_elements(A, B):
            setB = set(B)     # O(m)
            result = []

            for x in A:
                if x in setB:
                    result.append(x)

            return result
        final=common_elements(pp,pq)
        return final[-1]
        





        
