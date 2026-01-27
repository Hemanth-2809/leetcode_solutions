"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        new = {}
        def dfs(node):
            if node in new:
                return new[node]
            c = Node(node.val)
            new[node] = c
            for n in node.neighbors:
                c.neighbors.append(dfs(n))
            return c
        return dfs(node) if node else None

        
        
